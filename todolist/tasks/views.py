from django.shortcuts import render, redirect
from .models import User, Task
from django.contrib import messages
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

def index(request):
    if request.method == 'POST':
        request_dict = request.POST.dict()
        login = request_dict.get('login')
        password = request_dict.get('pswd')

        user = authenticate(username=login, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            request.session['user_id'] = user.id
            request.session['access_token'] = access_token
            request.session['refresh_token'] = refresh_token
            return redirect('home')

        else:
            messages.error(request, 'Usuário ou senha incorretos. Por favor, tente novamente.')
            return redirect('index')

    else:
        return render(request, 'tasks/index.html')


def signup(request):
    if request.method == 'POST':
        request_dict = request.POST.dict()
        login = request_dict.get('login')
        password = request_dict.get('pswd')

        if User.objects.filter(login=login).exists():
            messages.error(request, 'Usuário já existe. Por favor, escolha outro nome de usuário.')
            return redirect('signup')

        user = User(login=login)
        user.set_password(password)
        user.save()
        return redirect('index')

    else:
        return render(request, 'tasks/signup.html')


def home(request):
    if 'user_id' in request.session and 'access_token' in request.session:

        try:
            if JWTAuthentication().get_validated_token(request.session['access_token']):
                user = User.objects.get(id=request.session['user_id'])
                tasks = Task.objects.filter(user=user)
                return render(request, 'tasks/home.html', {'user': user, 'tasks': tasks})
            else:
                messages.error(request, 'Sua sessão expirou. Por favor, faça login novamente.')
                return redirect('index')

        except (InvalidToken, TokenError):
            messages.error(request, 'Sua sessão expirou. Por favor, faça login novamente.')
            return redirect('index')

    else:
        messages.error(request, 'Faça login para acessar esta página.')
        return redirect('index')