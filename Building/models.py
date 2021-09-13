from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Building(models.Model):
    street = models.CharField(max_length=100)
    building_no = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    no_of_flats = models.PositiveIntegerField()
    building_picture = models.ImageField(upload_to='images/')
    housing_cooperative = models.ForeignKey('HousingCooperative', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.street} {self.building_no}'

    def get_absolute_url(self):
        return reverse('building_detail', kwargs={'slug': self.slug})


PARCEL_PRECINCTS = [
    (1, 'Północ'),
    (2, 'Południe'),
    (3, 'Zachód'),
    (4, 'Wschód'),
]


class Cartography(models.Model):
    parcel_identification_number = models.CharField(max_length=30)
    parcel_precinct = models.SmallIntegerField(choices=PARCEL_PRECINCTS)
    parcel_number = models.CharField(max_length=20)
    building = models.OneToOneField('Building', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.building} - {self.parcel_identification_number}'

    def get_absolute_url(self):
        return reverse('cartography_detail', args=[str(self.id)])


class HousingCooperative(models.Model):
    name = models.CharField(max_length=100)
    president = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name.title()}'

    def get_absolute_url(self):
        return reverse('housing_cooperative_detail', args=[str(self.id)])
# https://mapy.geoportal.gov.pl/imap/Imgp_2.html?identifyParcel=026401_1.0022.AR_28.87/14
