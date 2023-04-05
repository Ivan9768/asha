from django.urls import path, include
from . import views
from main.views import home, auth, vkauth, logout_view


urlpatterns = [
    path('', home, name='home'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('auth/', auth, name='auth'),

    path('vkauth/', vkauth, name='vkauth'),
    path('logout/', logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]