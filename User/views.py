from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, ListView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

from Building.models import Flat
from User.forms import SignUpForm, ProfileFormAdditional, ProfileFlatForm
from User.models import Profile


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('User:profile_create_additional')
    template_name = 'User/signup.html'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('User:signup')
    template_name = 'User/change_pass.html'


class ProfileCreateAdditionalView(LoginRequiredMixin, CreateView):
    form_class = ProfileFormAdditional
    success_url = reverse_lazy('User:profile_creation_flat/')
    template_name = 'User/profile_create_additional.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def get_object(self, queryset=None):
        return self.request.user


class FlatFormView(FormView):
    model = Profile
    template_name = 'User/profile_create_flat.html'
    form_class = ProfileFlatForm
    context_object_name = 'flat'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('Building:flat_details', kwargs={'slug': self.kwargs.get('slug'),
                                                             'pk': self.kwargs.get('pk')})

# class FlatFormView(LoginRequiredMixin, UpdateView):
#     form_class = ProfileFlatForm
#     template_name = 'User/profile_create_flat.html'
#     success_url = reverse_lazy('User:signup')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def get_initial(self):
#         return {
#             'user': self.request.user,
#         }
#
#     def get_object(self, queryset=None):
#         return self.request.user


class FlatUserUpdateView(UpdateView):
    model = Flat
    template_name = 'User/profile_create_flat.html'
    success_url = reverse_lazy('User:signup')


# def load_flats(request):
#     building_id = request.GET.get('building')
#     flats = Flat.objects.filter(building_id=building_id).order_by('street', 'number')
#     return render(request, 'User/flat_building_list.html', {'flats': flats})


# class ProfileCreateBuildingView(LoginRequiredMixin, UpdateView):
#     form_class = ProfileFormBuilding
#     success_url = reverse_lazy('User:profile_create_flat')
#     template_name = 'User/profile_create_building.html'
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def get_initial(self):
#         return {
#             'user': self.request.user,
#         }


# class ProfileCreateFlatView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class = ProfileFormFlat
#     # success_url = reverse_lazy('User:profile')
#     template_name = 'User/profile_create_flat.html'
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile
#
#     def get_success_url(self):
#         print(self.object, self.object.building.building.slug, self.object.flat.pk)
#         return reverse_lazy('Building:flat_update',
#                             kwargs={'slug': self.object.building.building.slug, 'pk': self.object.flat.pk})


# def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)
#
# def get_initial(self):
#     return {
#         'user': self.request.user,
#     }
#
# def get_form(self, form_class=None):
#     buildings = self.object.building.all()
#     form = ProfileFormFlat(buildings=buildings)
#     return form


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'User/profile_view.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
    #
    # def get_queryset(self):
    #     return Profile.objects.get(user=self.request.user)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('User:main')
    template_name = 'User/login.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('User:main')


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')
