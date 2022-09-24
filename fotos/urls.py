from django.urls import path

from . import views

app_name = 'fotos'

urlpatterns = [
    path("", views.galeria, name='galeria'),
    path("agregar/", views.agregar, name="agregar"),
    path("foto/<str:pk>/", views.foto, name="foto"),
]
