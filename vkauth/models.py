from django.contrib.auth.models import AbstractUser
from django.db import models

class VKUser(AbstractUser):
    nickname = models.CharField(max_length=14, default='Игрок')
    password = models.CharField(max_length=128, default='')
    photo_path = models.FileField(blank=True, upload_to='photos/user_pfotos')

    def __str__(self):
        return self.nickname