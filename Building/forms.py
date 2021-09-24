from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Building.models import Building, Flat, BuildingPhotos
from User.models import Profile


class BuildingPhotosForm(forms.ModelForm):
    class Meta:
        model = BuildingPhotos
        # exclude = ['building']
        fields = '__all__'
        labels = {
            'picture_description': 'Opis zdjęcia',
            'picture': ''
        }
