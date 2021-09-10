from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from User.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label='Użytkownik', widget=forms.TextInput(
        attrs={'placeholder': '150 lub mniej znaków'}))
    first_name = forms.CharField(max_length=30, required=True, label='Imię')
    last_name = forms.CharField(max_length=30, required=True, label='Nazwisko')
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'placeholder': 'email musi być poprawny'}))
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Minimum 8 znaków, cyfry i litery',
                                label='Hasło', )
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

