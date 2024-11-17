from django.shortcuts import render, redirect
from .models import User, Task

def index(request):
    if request.method == 'POST':
        request = request.POST.dict()
        print(request)
        # login = request.get('login')
        # password = request.get('senha')
        # # Print alert with login and password
        # print(f'Login: {login}, Password: {password}')
        return redirect('index')
    else:
        return render(request, 'tasks/index.html')


def signup(request):
    if request.method == 'POST':
        print("POST ====> " + str(request.POST.dict()))
        # Print alert with login and password
        # print(f'Login: {login}, Password: {password}')
        # user = User(login=login, password=password)
        # user.save()

        return redirect('signup')
    else:
        return render(request, 'tasks/signup.html')
