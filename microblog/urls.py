from django.urls import path

from .views import perfil

urlpatterns = [
    path('<str:user>/', perfil)
]
