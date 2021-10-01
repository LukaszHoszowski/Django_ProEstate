from django import forms

from Building.models import Building, Flat, BuildingPhotos, BuildingDocs, Measure


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
        exclude = ['building', 'slug_flat', 'number', 'user']
        help_texts = {
            'number_suffix': 'podaj suffix mieszkania jeśli istnieje',
            'area': 'powierzchnia w ㎡',
            'floor': 'piętro',
            'ownership_type': 'typ własności',
            'heating_type': 'typ ogrzewania',
            'water_heating': 'podgrzewanie wody z CO',
            'natural_gas': 'gaz',
            'electricity': 'prąd',
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


class MeasureUpdateForm(forms.ModelForm):
    class Meta:
        model = Measure
        exclude = ['flat', 'payment_period']
        help_texts = {
            'gas': 'podaj wskazania gazomierza',
            'energy': 'podaj wskazania licznika energii elektrycznej',
            'water': 'podaj wskazania wodomierza',
        }
        labels = {
            'gas': '',
            'energy': '',
            'water': '',
        }
