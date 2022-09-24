from unicodedata import category

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Categoria, Foto


# Create your views here.
def galeria(request):
    cat = request.GET.get('categoria')

    if cat == None:
        fotos = Foto.objects.all()
    else:
        fotos = Foto.objects.filter(categoria__nommbre=cat)

    categorias = Categoria.objects.all()
    context = {'categorias': categorias, 'fotos': fotos}
    return render(request, "fotos/galeria.html", context)


def agregar(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        data = request.POST
        imagen = request.FILES.get('foto')

        if data['categoria'] != 'none':
            categoria = Categoria.objects.get(id=data['categoria'])

        elif data['nueva_categoria'] != '':
            categoria, creado = Categoria.objects.get_or_create(
                nommbre=data['nueva_categoria'])

        else:
            categoria = None

        foto = Foto.objects.create(
            categoria=categoria,
            descripcion=data['descripcion'],
            foto=imagen,
        )

        return redirect('fotos:galeria')

    context = {'categorias': categorias}
    return render(request, "fotos/agregar.html", context)


def foto(request, pk):
    foto = Foto.objects.get(id=pk)
    context = {'foto': foto}
    return render(request, "fotos/foto.html", context)
