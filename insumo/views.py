from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import InsumoForm
from .models import Insumo, Categoria 

#----------------------------------------------------------------------------------------------------------

def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo insumo en la base de datos
            return redirect('insumos:lista_insumos')  # Redirige a la lista de insumos después de agregar uno
    else:
        form = InsumoForm()

    return render(request, 'insumo/agregar_insumo.html', {'form': form})

#----------------------------------------------------------------------------------------------------------

def listar_insumos(request):
    insumos = Insumo.objects.all()  # Obtener todos los insumos
    return render(request, 'insumo/list_insumos.html', {'insumos': insumos})

#----------------------------------------------------------------------------------------------------------

def administrar_categorias(request):
    if request.method == "POST":
        nueva_categoria = request.POST.get("nueva_categoria")
        if nueva_categoria:
            Categoria.objects.get_or_create(nombre=nueva_categoria)
            messages.success(request, "Categoría agregada correctamente.")
        return redirect("insumos:administrar_categorias")

    categorias = Categoria.objects.all()
    return render(request, "insumo/administrar_categorias.html", {"categorias": categorias})

#----------------------------------------------------------------------------------------------------------

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    messages.success(request, "Categoría eliminada correctamente.")
    return redirect("insumos:administrar_categorias")

#----------------------------------------------------------------------------------------------------------