from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from social_django.utils import load_strategy
from social_django.models import UserSocialAuth
from vkauth.models import VKUser
from django.conf import settings


def auth(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {'client_id': settings.SOCIAL_AUTH_VK_OAUTH2_KEY}
        return render(request, 'vkauth/auth.html')


def vkauth(request):
    if request.GET.get('code'):
        # Подключаем стратегию для работы с соцсетями
        strategy = load_strategy(request)

        # Получаем токен VK из запроса
        code = request.GET.get('code')
        user = request.user

        # Проверяем, что пользователь залогинен
        if not user.is_authenticated:
            return redirect('auth')

        social = UserSocialAuth.get_social_auth_for_user(user)[0]
        response = social.get_access_token(code)
        vk_token = response.get('access_token')

        # Получаем данные о пользователе из VK API
        social = UserSocialAuth.objects.get(user=request.user)
        user_data = social.extra_data
        vk_id = user_data['id']
        namefull = user_data['first_name']
        password = ''

        # Сохраняем данные пользователя в БД
        vk_user = VKUser.objects.create(vk_id=vk_id, password=password)


        # Авторизуем пользователя в Django
        user = authenticate(request=request, vk_id=vk_id, password=password)
        login(request, user)

        return redirect('home')
    else:
        # Если токен отсутствует, перенаправляем пользователя на страницу авторизации VK
        if not request.user.is_authenticated:
            return redirect('auth')

        social = UserSocialAuth.get_social_auth_for_user(request.user)[0]
        auth_url = social.get_redirect_url(request, process='login')
        return redirect(auth_url)

def logout_view(request):
    logout(request)
    return redirect('auth')