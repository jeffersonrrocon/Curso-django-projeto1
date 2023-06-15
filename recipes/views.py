from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'JRR',
    })


def sobre(request):
    return HttpResponse('sobre 2')


def contato(request):
    return render(request, 'recipes/contato.html')
