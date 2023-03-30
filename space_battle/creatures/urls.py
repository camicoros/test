from django.urls import path

from .views import index, aliens, spaceships, spacemans

urlpatterns = [
    path('', index, name='index'),
    path('aliens/', aliens, name='aliens'),
    path('battleships/', spaceships, name='spaceships'),
    path('spacemans/', spacemans, name='spacemans')
]