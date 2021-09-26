from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from Building.models import Building, Flat


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)
    contact_flag = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default=None, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/avatars/', null=True, blank=True, verbose_name='Avatar użytkownika')
    building = models.ManyToManyField(Building, blank=True)
    # usunac i zostawic relacje profile -> flat
    flat = models.ManyToManyField(Flat, blank=True)

    # def get_queryset(self, request):
    #     queryset = Profile.objects.filter(user=request.user)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
