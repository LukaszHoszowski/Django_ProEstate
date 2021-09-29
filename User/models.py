from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from Building.models import Building, Flat


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[RegexValidator(regex=r"^\+?1?\d{8,15}$")], max_length=16, unique=True,
                                    blank=True)
    contact_flag = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default=None, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/avatars/', null=True, blank=True,
                               verbose_name='Avatar użytkownika')

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
