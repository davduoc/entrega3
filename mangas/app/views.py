from django.shortcuts import render, redirect, get_object_or_404
from .forms import MangaForm
from .models import Manga
# Create your views here.


def pagina_1Ecchi(request):
    return render(request, 'app/1Ecchi.html')

def pagina_1Josei(request):
    return render(request, 'app/1Josei.html')

def pagina_1Seinen(request):
    return render(request, 'app/1Seinen.html')

def pagina_1Shojo_ai(request):
    return render(request, 'app/1Shojo_ai.html')

def pagina_1Shojo(request):
    return render(request, 'app/1Shojo.html')

def pagina_1Shonen_ai(request):
    return render(request, 'app/1Shonen_ai.html')

def pagina_1Shonen(request):
    return render(request, 'app/1Shonen.html')

def pagina_1Yaoi(request):
    return render(request, 'app/1Yaoi.html')

def pagina_1Yuri(request):
    return render(request, 'app/1Yuri.html')

def pagina_buscar(request):
    return render(request, 'app/buscar.html')

def pagina_buscart(request):
    return render(request, 'app/buscart.html')

def pagina_carrito(request):
    return render(request, 'app/carrito.html')

def pagina_catalogo(request):
    return render(request, 'app/catalogo.html')

def pagina_confirmarcompra(request):
    return render(request, 'app/confirmarcompra.html')

def pagina_contacto(request):
    return render(request, 'app/contacto.html')

def pagina_contacto2(request):
    return render(request, 'app/contacto2.html')

def pagina_en_construccion(request):
    return render(request, 'app/en_construccion.html')

def pagina_index(request):
    return render(request, 'app/index.html')

def pagina_inicio_sesion(request):
    return render(request, 'app/inicio_sesion.html')

def pagina_plantilla(request):
    return render(request, 'app/plantilla.html')

def pagina_prueba_2(request):
    return render(request, 'app/prueba_2.html')

def pagina_registro(request):
    return render(request, 'app/registro.html')





def manga_list(request):
    mangas = Manga.objects.all()
    return render(request, 'app/manga_list.html', {'mangas': mangas})

def manga_create(request):
    if request.method == 'POST':
        form = MangaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manga_list')
    else:
        form = MangaForm()
    return render(request, 'app/manga_form.html', {'form': form})

def manga_update(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    if request.method == 'POST':
        form = MangaForm(request.POST, instance=manga)
        if form.is_valid():
            form.save()
            return redirect('manga_list')
    else:
        form = MangaForm(instance=manga)
    return render(request, 'app/manga_form.html', {'form': form})

def manga_delete(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    if request.method == 'POST':
        manga.delete()
        return redirect('manga_list')
    return render(request, 'app/manga_confirm_delete.html', {'manga': manga})