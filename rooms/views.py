from django.shortcuts import render

def rooms_home(request):
    return render(request, 'main/about.html')
