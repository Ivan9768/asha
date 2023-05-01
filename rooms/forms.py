from .models import Rooms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CheckboxInput, FileInput, NumberInput

class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ['name', 'about', 'image', 'game_place', 'public', 'date_show', 'access_room']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название комнаты',
            }),
            "about": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            "game_place": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите колличество игроков',
            }),
            "public": CheckboxInput(attrs={
            }),
            "date_show": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время открытия',
            }),
            "access_room": CheckboxInput(attrs={
            }),
        }