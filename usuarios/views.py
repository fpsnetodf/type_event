from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


# user = User.objects.filter(username=username)

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    elif request.method == 'POST':
        user = User.objects.filter(username=username)
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        print(username, email, senha,
              confirmar_senha)
        return HttpResponse('teste')
        