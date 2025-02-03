from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import InsumoForm
from .models import Insumo, Categoria 

#----------------------------------------------------------------------------------------------------------

def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST, request.FILES)  # ¡Aquí está el cambio!
        if form.is_valid():
            form.save()  # Guarda el nuevo insumo en la base de datos
            return redirect('insumos:listar_insumos')  # Redirige a la lista de insumos después de agregar uno
    else:
        form = InsumoForm()

    return render(request, 'insumo/agregar_insumo.html', {'form': form})

#----------------------------------------------------------------------------------------------------------

def listar_insumos(request):
    insumos = Insumo.objects.all()  # Obtener todos los insumos
    return render(request, 'insumo/list_insumos.html', {'insumos': insumos})

#----------------------------------------------------------------------------------------------------------

def ver_detalle_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)
    return render(request, 'insumo/ver_detalle_insumo.html', {'insumo': insumo})

#----------------------------------------------------------------------------------------------------------

def eliminar_insumo(request, insumo_id):
    insumo = get_object_or_404(Insumo, id=insumo_id)
    insumo.delete()
    messages.success(request, "Insumo eliminado correctamente.")
    return redirect('insumos:listar_insumos')

#----------------------------------------------------------------------------------------------------------

def administrar_categorias(request):
    categorias_list = Categoria.objects.all().order_by('nombre')  # Ordenar por nombre
    paginator = Paginator(categorias_list, 10)  # Mostrar 10 categorías por página

    page = request.GET.get('page')  # Obtener el número de página desde la URL
    try:
        categorias = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, mostrar la primera página
        categorias = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        categorias = paginator.page(paginator.num_pages)

    if request.method == "POST":
        nueva_categoria = request.POST.get("nueva_categoria")
        if nueva_categoria:
            Categoria.objects.get_or_create(nombre=nueva_categoria)
            messages.success(request, "Categoría agregada correctamente.")
        return redirect("insumos:administrar_categorias")

    return render(request, "insumo/category_administration.html", {"categorias": categorias})

#----------------------------------------------------------------------------------------------------------

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    messages.success(request, "Categoría eliminada correctamente.")
    return redirect("insumos:administrar_categorias")

#----------------------------------------------------------------------------------------------------------