from django.db import models


# Create your models here.
class Building(models.Model):
    street = models.CharField(max_length=100)
    building_no = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    no_of_flats = models.PositiveIntegerField()
    building_picture = models.ImageField(upload_to='images/')
    roof_keys_keeper = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street} {self.building_no}'


class Cartography(models.Model):
    parcel_identification_number = models.CharField(max_length=30)
    parcel_precinct = models.CharField(max_length=10)
    parcel_number = models.CharField(max_length=20)
    building = models.OneToOneField('Building', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.parcel_identification_number}'


class HousingCooperative(models.Model):
    name = models.CharField(max_length=100)
    president = models.ForeignKey('User', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name.title()}'

# https://mapy.geoportal.gov.pl/imap/Imgp_2.html?identifyParcel=026401_1.0022.AR_28.87/14
