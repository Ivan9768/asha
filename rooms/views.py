from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth

def rooms_home(request):
    if request.user.is_authenticated:
        try:
            social = UserSocialAuth.objects.get(user=request.user)
            photo_url = social.extra_data['photo_max_orig']
        except UserSocialAuth.DoesNotExist:
            photo_url = None

        return render(request, 'rooms/rooms_home.html', {'user': request.user, 'photo_url': photo_url})
    else:
        return redirect('auth')

def create_room(request):
    if request.user.is_authenticated:
        try:
            social = UserSocialAuth.objects.get(user=request.user)
            photo_url = social.extra_data['photo_max_orig']
        except UserSocialAuth.DoesNotExist:
            photo_url = None

        return render(request, 'rooms/create_room.html', {'user': request.user, 'photo_url': photo_url})
    else:
        return redirect('auth')
