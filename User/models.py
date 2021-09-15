from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    building = models.CharField(max_length=5, blank=True) # queryset / Foreingkey
    flat = models.CharField(max_length=5, blank=True)

    # def get_absolute_url(self):
    #     return reverse('author-detail', kwargs={'pk': self.pk})
