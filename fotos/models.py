from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Categoria(models.Model):
    nommbre = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.nommbre


class Foto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )
    foto = models.ImageField(null=False, blank=False)
    descripcion = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self) -> str:
        return self.descripcion
