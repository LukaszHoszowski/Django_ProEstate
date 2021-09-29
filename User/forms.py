from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Building.models import Building, Flat
from User.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Nazwa użytkownika'}), help_text='Nie więcej niż 150 znaków')
    first_name = forms.CharField(max_length=30, required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=30, required=True, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Nazwisko'}))
    email = forms.EmailField(max_length=254, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Hasło, minimum 8 znaków, cyfry i litery',
                                label='')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Powtórz hasło',
                                label='')

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
            'avatar': '',
            'phone_number': '',
            'contact_flag': '',
        }
        help_texts = {
            'contact_flag': """Czy wyrażasz zgodę na udostępnianie Twoich informacji kontaktowych innym mieszkańcom. 
            Jeśli nie wyrazisz zgody, nikt nie będzie mógł Cie poinformować o awariach i innych zdarzeniach.""",
            'avatar': 'Dodaj swoje zdjęcie',
            'phone_number': 'Dodaj swój nr telefonu',
        }


class ProfileFlatForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['flat']
        labels = {
            'flat': '',
        }
        help_texts = {
            'flat': 'Wybierz swoje mieszkanie',
        }


class EmailForm(forms.Form):
    FAILURES = [
        ('Wybierz typ awarii', 'Wybierz typ awarii'),
        ('Zalanie', 'Zalanie'),
        ('Uszkodzenie', 'Uszkodzenie')
    ]

    failure_building = forms.ModelChoiceField(queryset=Building.objects.all(), label='',
    empty_label = 'Wybierz budynek którego dotyczy awaria', required = False)
    failure_flat = forms.CheckboxInput()
    failure_type = forms.ChoiceField(choices=FAILURES, label='', required=False)
    # subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Temat wiadomości'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Treść wiadomości'}))

    # class FlatUserForm(forms.ModelForm):
    #     class Meta:
    #         model = Flat
    #         fields = ('building', 'flat')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['flat'].queryset = Flat.objects.none()
    #     # self.fields['building'].queryset = Flat.objects.none()

    # class ProfileFormBuilding(forms.ModelForm):
    #     class Meta:
    #         model = Profile
    #         fields = ['building']
    #         labels = {
    #             'building': 'Budynek',
    #         }

    # class ProfileFormFlat(forms.ModelForm):
    #     class Meta:
    #         model = Profile
    #         fields = ['flat']
    #         # fields = '__all__'
    #         labels = {
    #             'flat': 'Mieszkanie',
    #         }

    # def __init__(self, *args, buildings=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if buildings is not None:
    #         self.fields['flat'].queryset = Flat.objects.filter(building__id__in=buildings)
