from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Building.models import Building, Flat
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


class ProfileFormAdditional(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'phone_number', 'contact_flag']
        labels = {
            'avatar': 'Dodaj swoje zdjęcie',
            'phone_number': 'Nr telefonu',
            'contact_flag': '',
        }
        help_texts = {
            'contact_flag': """Czy wyrażasz zgodę na udostępnianie Twoich informacji kontaktowych innym mieszkańcom. 
            Jeśli nie wyrazisz zgody, nikt nie będzie mógł Cie poinformować o awariach i innych zdarzeniach."""
        }


class ProfileFormBuilding(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['building']
        labels = {
            'building': 'Budynek',
        }




class ProfileFormFlat(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['flat']
        # fields = '__all__'
        labels = {
            'flat': 'Mieszkanie',
        }

    def __init__(self, *args, buildings=None, **kwargs):
        super().__init__(*args, **kwargs)
        if buildings is not None:
            self.fields['flat'].queryset = Flat.objects.filter(building__id__in=buildings)
