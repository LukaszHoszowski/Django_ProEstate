from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from User.forms import SignUpForm, ProfileForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('profile_create')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('signup')
    template_name = 'change_pass.html'


class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('signup')
    template_name = 'profile_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('signup')
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('signup')
