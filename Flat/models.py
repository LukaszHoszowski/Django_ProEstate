from django.contrib.auth.models import User
from django.db import models

from Building.models import Building

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


class Flat(models.Model):
    number = models.PositiveIntegerField(verbose_name='Nr mieszkania')
    number_suffix = models.CharField(max_length=1, null=True, blank=True, default=None, verbose_name='Suffix',
                                     choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),
                                              ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'),
                                              ('M', 'M')])
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
