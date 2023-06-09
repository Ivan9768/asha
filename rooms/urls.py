from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_home, name='rooms_home'),
    path('create_room', views.create_room, name='create_room'),
    path(r'^delete/(?P<id>[0-9]+)/$', views.delete_room, name='delete_room'),
]