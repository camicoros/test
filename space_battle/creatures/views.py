from django.shortcuts import render

from .models import SpaceMan


def index(request):
    return render(request, 'creatures/index.html', {'title': 'all creatures'})


def aliens(request):
    return render(request, 'creatures/index.html', {'title': 'aliens'})


def spaceships(request):
    return render(request, 'creatures/index.html', {'title': 'spaceships'})


def spacemans(request):

    spacemans_from_db = SpaceMan.objects.all()

    return render(request, 'creatures/index.html', {
        'title': 'spacemans',
        'spacemans': ['Юрий Гагарин', 'Нилл Армстронг', 'Валентина Терешкова'],
        'spacemans_from_db': spacemans_from_db,
    })
