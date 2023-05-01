from django.shortcuts import render, redirect, get_object_or_404
from .forms import RoomForm
from .models import Rooms
from vkauth.models import VKUser
import os
from django.conf import settings

def rooms_home(request):
    if request.user.is_authenticated:
        rooms = Rooms.objects.all()
        my_objects = VKUser.objects.all()
        context = {'rooms': rooms, 'my_objects': my_objects}
        return render(request, 'rooms/rooms_home.html', context)
    else:
        return redirect('auth')

# def create_room(request):
#     if request.user.is_authenticated:
#         try:
#             social = UserSocialAuth.objects.get(user=request.user)
#             photo_url = social.extra_data['photo_max_orig']
#         except UserSocialAuth.DoesNotExist:
#             photo_url = None
#
#         return render(request, 'rooms/create_room.html', {'user': request.user, 'photo_url': photo_url})
#     else:
#         return redirect('auth')

def create_room(request):
    error = ''
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # photo = form.cleaned_data['image']
            # with open(os.path.join(settings.ROOM_PHOTOS_ROOT, photo.name), 'wb+') as destination:
            #     for chunk in photo.chunks():
            #         destination.write(chunk)
            return redirect('rooms_home')
        else:
            error = form.errors
    form = RoomForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'rooms/create_room.html', data)
def delete_room(request, id):
    room = get_object_or_404(Rooms, id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('/')

    return render(request, 'rooms/rooms_home.html', {'room': room})