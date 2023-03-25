from django.urls import path
from . import views
urlpatterns = [
    path('', views.rooms_home, name='rooms_home'),
]