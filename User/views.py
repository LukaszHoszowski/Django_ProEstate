from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

from Building.models import Flat
from User.forms import SignUpForm, ProfileFormAdditional, ReportFailureForm, ContactNeighbourForm, \
    ProfileUpdateForm, ProfileFlatForm, ContactUsForm
from User.user_helper_functions import create_email_subject_neighbour, create_email_message_neighbour, \
    create_email_subject_failure, create_email_message_failure
from User.models import Profile
from proestate.settings import EMAIL_HOST_USER


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


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
    success_url = reverse_lazy('User:profile_create_flat')
    template_name = 'User/profile_create_additional.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FlatUserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileFlatForm()
        return render(request, 'User/profile_create_flat.html', {'form': form})

    def post(self, request):
        form = ProfileFlatForm(request.POST)

        if form.is_valid():
            flat = Flat.objects.get(id=form['flat'].value())
            flat.user.add(request.user)
            flat.save()
        else:
            form = ProfileFlatForm()
            return render(request, 'User/profile_create_flat.html', {
                'form': form,
            })

        return redirect('Building:flat_update', slug=flat.building.slug, pk=flat.pk)


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    exclude = ['is_verified', 'token']
    template_name = 'User/profile_view.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'User/profile_update_view.html'
    success_url = reverse_lazy('User:profile')

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


class ReportFailureView(LoginRequiredMixin, View):
    def get(self, request):
        form = ReportFailureForm()
        return render(request, 'User/profile_report_failure.html', {'form': form})

    def post(self, request):
        form = ReportFailureForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            subject = create_email_subject_failure(cd['failure_building'], cd['failure_type'])

            message = cd['message']
            message += create_email_message_failure(self.request.user.first_name,
                                                    self.request.user.last_name,
                                                    self.request.user.email,
                                                    self.request.user,
                                                    self.request.user.flat_set.first(),
                                                    cd['failure_building'],
                                                    cd['failure_type'])

            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        else:
            form = ReportFailureForm()
            return render(request, 'User/profile_report_failure.html', {
                'form': form,
            })

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class ContactNeighbourView(LoginRequiredMixin, View):
    def get(self, request):
        form = ContactNeighbourForm()
        return render(request, 'User/profile_contact_neighbour.html', {'form': form})

    def post(self, request):
        form = ContactNeighbourForm(request.POST)

        if form.is_valid():
            recipients_query = Profile.objects.filter(user__flat=form['flat'].value())
            recipients = [recipient.user.email for recipient in recipients_query]

            subject = create_email_subject_neighbour(self.request.user.first_name, self.request.user.last_name,
                                                     self.request.user)

            message = create_email_message_neighbour(self.request.user.flat_set.first(),
                                                     self.request.user.profile.phone_number,
                                                     self.request.user.email, self.request.user.first_name,
                                                     self.request.user.last_name)

            send_mail(subject, message, EMAIL_HOST_USER, recipients)
        else:
            form = ContactNeighbourForm()
            return render(request, 'User/profile_contact_neighbour.html', {
                'form': form,
            })

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'contact_us.html', {'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            subject = 'Mail z proEstate'

            message = cd['message']
            message += f'''
            
            Mail od {cd["email"]}
            '''

            send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        else:
            form = ReportFailureForm()
            return render(request, 'contact_us.html', {
                'form': form,
            })

        return redirect('main')
