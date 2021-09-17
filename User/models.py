from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from Building.models import Building, Flat


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)
    building = models.ManyToManyField(Building, blank=True)
    flat = models.ManyToManyField(Flat, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default=None)

    # def get_absolute_url(self):
    #     return reverse('author-detail', kwargs={'pk': self.pk})
