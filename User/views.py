from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from User.forms import SignUpForm, ProfileFormBuilding, ProfileFormFlat
from User.models import Profile


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('User:profile_create_building')
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


class ProfileCreateBuildingView(LoginRequiredMixin, CreateView):
    form_class = ProfileFormBuilding
    success_url = reverse_lazy('User:profile_create_flat')
    template_name = 'User/profile_create_building.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileCreateFlatView(LoginRequiredMixin, CreateView):
    form_class = ProfileFormFlat
    success_url = reverse_lazy('User:profile')
    template_name = 'User/profile_create_flat.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'User/profile_view.html'

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('User:signup')
    template_name = 'User/login.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('signup')


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')
