from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import TemplateView

# Create your views here.
def cadastro(request):
    return render(request, 'usuarios/cadastro.html')