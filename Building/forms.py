from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Building.models import Building, Flat, BuildingPhotos, BuildingDocs
from User.models import Profile


class BuildingPhotosForm(forms.ModelForm):
    class Meta:
        model = BuildingPhotos
        exclude = ['building']
        labels = {
            'picture_description': 'Opis zdjęcia',
            'picture': '',
        }


class BuildingDocsForm(forms.ModelForm):
    class Meta:
        model = BuildingDocs
        exclude = ['building']
        labels = {
            'document_description': 'Opis dokumentu',
            'document': '',
        }


class FlatUpdateForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ['building', 'slug', 'number']
        help_texts = {
            'number_suffix': 'podaj suffix mieszkania jeśli istnieje',
            'area': 'powierzchnia w ㎡',
            'floor': 'piętro',
            'ownership_type': 'typ własności',
            'heating_type': 'typ ogrzewania',
            'water_heating': 'podgrzewanie wody z CO',
            'natural_gas': 'gaz',
            'electricity': 'prad',
            'water': 'woda',
        }
        labels = {
            'number_suffix': '',
            'area': '',
            'floor': '',
            'ownership_type': '',
            'heating_type': '',
            'water_heating': '',
            'natural_gas': '',
            'electricity': '',
            'water': '',
        }
