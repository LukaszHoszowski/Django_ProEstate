from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

from Building.models import Flat, Building
from User.forms import SignUpForm, ProfileFormAdditional, ProfileFlatForm, EmailForm
from User.models import Profile
from proestate.settings import EMAIL_HOST_USER


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


class ProfileCreateAdditionalView(LoginRequiredMixin, CreateView):
    form_class = ProfileFormAdditional
    success_url = reverse_lazy('User:profile_creation_flat')
    template_name = 'User/profile_create_additional.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FlatFormView(UpdateView):
    model = Profile
    template_name = 'User/profile_create_flat.html'
    form_class = ProfileFlatForm
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        return context

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


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'User/profile_view.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('User:main')
    template_name = 'User/login.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('User:main')


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('User:signup')
    template_name = 'User/change_pass.html'


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('User:user_logout')
    template_name = 'User/user_confirm_delete.html'

    def get_object(self, queryset=None):
        return self.request.user


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class ContactView(View):
    def get(self, request):
        form = EmailForm()
        return render(request, 'User/profile_contact.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Zgłoszenie awarii - {cd['failure_building']} - {cd['failure_type']}"
            message = cd['message']
            message += f"""
            
            urzytkownik:    {self.request.user.first_name} {self.request.user.last_name} / {self.request.user.email} / {self.request.user}
            budynek:        {cd['failure_building']}
            typ awarii:     {cd['failure_type']}
            
            """

            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
            messageSent = True
        else:
            form = EmailForm()
        return render(request, 'User/profile_contact.html', {
            'form': form,
            'messageSent': messageSent,
        })
