from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from social_django.utils import load_strategy
from social_django.models import UserSocialAuth
from main.models import VKUser



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return redirect('auth')


def auth(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'auth.html')


def vkauth(request):
    if request.GET.get('code'):
        # Подключаем стратегию для работы с соцсетями
        strategy = load_strategy(request)

        # Получаем токен VK из запроса
        code = request.GET.get('code')
        user = request.user
        social = UserSocialAuth.get_social_auth_for_user(user)[0]
        response = social.get_access_token(code)
        vk_token = response.get('access_token')

        # Получаем данные о пользователе из VK API
        user_data = social.extra_data
        vk_id = user_data['id']
        first_name = user_data['first_name']
        last_name = user_data['last_name']
        photo = user_data['photo_200']

        # Сохраняем данные пользователя в БД
        vk_user, created = VKUser.objects.get_or_create(vk_id=vk_id)
        vk_user.first_name = first_name
        vk_user.last_name = last_name
        vk_user.photo = photo
        vk_user.save()

        # Авторизуем пользователя в Django
        user = authenticate(request=request, username=vk_id, password=vk_token)
        login(request, user)

        return redirect('home')
    else:
        # Если токен отсутствует, перенаправляем пользователя на страницу авторизации VK
        social = UserSocialAuth.get_social_auth_for_user(request.user)[0]
        auth_url = social.get_redirect_url()
        return redirect(auth_url)
def logout_view(request):
    logout(request)
    return redirect('about')