from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

NUMBER_SUFFIX = [
    ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'),
    ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M')
]

PARCEL_PRECINCTS = [
    (1, 'Północ'),
    (2, 'Południe'),
    (3, 'Zachód'),
    (4, 'Wschód'),
]

OWNERSHIP_TYPES = [
    (1, 'Pełna własność'),
    (2, 'Spółdzielcze'),
    (3, 'Komunalne'),
]

HEATING_TYPES = [
    (1, 'CO'),
    (2, 'Gazowe'),
    (3, 'Elektryczne'),
    (4, 'Węglowe'),
]


class Building(models.Model):
    street = models.CharField(max_length=100, verbose_name='Ulica')
    building_no = models.CharField(max_length=5, verbose_name='Number budynku')
    city = models.CharField(max_length=100, verbose_name='Miasto')
    zip_code = models.CharField(max_length=6, verbose_name='Kod pocztowy')
    no_of_flats = models.PositiveIntegerField(verbose_name='Ilość mieszkań w budynku')
    building_picture = models.ImageField(upload_to='images/', verbose_name='Zdjęcie budynku')
    housing_cooperative = models.ForeignKey('HousingCooperative', on_delete=models.SET_NULL, null=True,
                                            verbose_name='Wspólnota/zarządca')
    slug = models.SlugField(null=False, unique=True)

    def generate_flats(self):
        for flat_no in range(self.no_of_flats):
            Flat.objects.create(number=flat_no + 1, building=self)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        creation = self.id is None
        super().save(force_insert, force_update, using,
                     update_fields)
        if creation:
            self.generate_flats()

    class Meta:
        ordering = ('street', 'building_no')
        verbose_name = 'Budynek'
        verbose_name_plural = 'Budynki'

    def __str__(self):
        return f'{self.street} {self.building_no}'

    def get_absolute_url(self):
        return reverse('building_detail', kwargs={'slug': self.slug})


class Cartography(models.Model):
    parcel_identification_number = models.CharField(max_length=30, verbose_name='Identyfikator działki')
    parcel_precinct = models.SmallIntegerField(choices=PARCEL_PRECINCTS, verbose_name='Obręb')
    parcel_number = models.CharField(max_length=20, verbose_name='Numer działki')
    building = models.OneToOneField('Building', on_delete=models.CASCADE, primary_key=True, verbose_name='Budynek')

    def __str__(self):
        return f'{self.building} - {self.parcel_identification_number}'

    def get_absolute_url(self):
        return reverse('cartography_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Dane kartograficzne'
        verbose_name_plural = 'Dane kartograficzne'


class HousingCooperative(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa zarządcy/wspólnoty')
    president = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Prezes')
    street = models.CharField(max_length=100, null=True, verbose_name='Ulica')
    number = models.CharField(max_length=10, null=True, verbose_name='Numer')
    city = models.CharField(max_length=100, null=True, verbose_name='Miasto')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='Kod pocztowy')
    logo = models.ImageField(upload_to='images/coop_logo/', null=True, verbose_name='Logotyp zarzadcy/wspólnoty')
    email = models.EmailField(max_length=254, null=True, verbose_name='Email')
    phone = models.CharField(max_length=12, null=True, verbose_name='Nr telefonu')

    def __str__(self):
        return f'{self.name.title()}'

    def get_absolute_url(self):
        return reverse('housing_cooperative_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Wspólnota/Zarządca'
        verbose_name_plural = 'Wspólnoty/Zarządcy'


class Flat(models.Model):
    number = models.PositiveIntegerField(verbose_name='Nr mieszkania')
    number_suffix = models.CharField(max_length=1, null=True, blank=True, default=None, verbose_name='Suffix',
                                     choices=NUMBER_SUFFIX)
    area = models.PositiveIntegerField(verbose_name='Powierzchnia w m2', null=True, blank=True)
    floor = models.SmallIntegerField(verbose_name='Piętro', null=True, blank=True)
    ownership_type = models.SmallIntegerField(choices=OWNERSHIP_TYPES, verbose_name='Typ własności', default=1)
    heating_type = models.SmallIntegerField(choices=HEATING_TYPES, verbose_name='Typ ogrzewania', default=1)
    natural_gas = models.BooleanField(default=True, verbose_name='Gaz')
    electricity = models.BooleanField(default=True, verbose_name='Prąd')
    water = models.BooleanField(default=True, verbose_name='Woda')
    water_heating = models.BooleanField(default=True, verbose_name='Podgrzewanie wody z CO')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Budynek')
    user = models.ManyToManyField(User, blank=True, verbose_name='Mieszkańcy')

    def __str__(self):
        return f'{self.building}/{self.number}{self.number_suffix if self.number_suffix else ""}'

    # def get_absolute_url(self):
    #     return reverse('flat_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Mieszkanie'
        verbose_name_plural = 'Mieszkania'

# https://mapy.geoportal.gov.pl/imap/Imgp_2.html?identifyParcel=026401_1.0022.AR_28.87/14
