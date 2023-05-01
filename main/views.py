from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from  vkauth.models import VKUser
from django.shortcuts import get_object_or_404


def about(request):
    if request.user.is_authenticated:
        my_objects = VKUser.objects.all()
        context = {'my_objects': my_objects}
        return render(request, 'main/about.html', context)
    else:
        return redirect('auth')

def home(request):
    if request.user.is_authenticated:
        id = request.user.id
        my_object = VKUser.objects.get(id=id)
        context = {'my_object': my_object}
        return render(request, 'main/index.html', context)
    else:
        return redirect('auth')
def profile(request):
    if request.user.is_authenticated:
        my_objects = VKUser.objects.all()
        context = {'my_objects': my_objects}

        return render(request, 'main/profile.html', context)
    else:
        return redirect('auth')