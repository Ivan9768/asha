from django.urls import path, include
from . import views
from vkauth.views import auth, vkauth, logout_view


urlpatterns = [
    path('', auth, name='auth'),

    path('vkauth/', vkauth, name='vkauth'),
    path('logout/', logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]