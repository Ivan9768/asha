from django.db import models
import random
from django.utils import timezone

class Rooms(models.Model):
    room_id = models.AutoField('Номер комнаты', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    about = models.TextField(max_length=500, verbose_name='Описание')
    image = models.FileField('Фото', upload_to='photos/rooms_photos')
    game_place = models.IntegerField('Колличество участников')
    public = models.BooleanField('Публичный доступ')
    date_show = models.DateTimeField('Дата и время проведения')
    access_room = models.BooleanField('Доступ сейчас')
    date_create = models.DateTimeField('Дата и время создания', auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.room_id:
            max_id = Rooms.objects.all().aggregate(models.Max('room_id'))['room_id__max']
            if max_id is not None:
                self.room_id = max_id + random.randint(1, 9)
            else:
                self.room_id = 100000
        super(Rooms, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
