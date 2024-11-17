from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        request = request.POST.dict()
        print(request)
        # login = request.get('login')
        # password = request.get('senha')
        # # Print alert with login and password
        # print(f'Login: {login}, Password: {password}')
        # return redirect('index')
    else:
        return render(request, 'tasks/index.html')


def signup(request):
    if request.method == 'POST':
        request_dict = request.POST.dict()
        login = request_dict.get('login')
        password = request_dict.get('pswd')
        # Check if user already exists
        if User.objects.filter(login=login).exists():
            messages.error(request, 'Usuário já existe. Por favor, escolha outro nome de usuário.')
            return redirect('signup')

        user = User(login=login, password=password)
        user.save()

        return redirect('signup')
    else:
        return render(request, 'tasks/signup.html')
