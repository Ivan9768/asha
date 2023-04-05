from django.contrib.auth.models import AbstractUser
from django.db import models

class VKUser(AbstractUser):
    vk_id = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, default='')
    photo_url = models.URLField()
    def __str__(self):
        return self.username