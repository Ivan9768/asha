from django.db import models

class VKUser(models.Model):
    vk_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    photo_url = models.URLField()

    def __str__(self):
        return self.name