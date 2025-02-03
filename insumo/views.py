from django.shortcuts import render, redirect
from .forms import InsumoForm
from .models import Insumo 

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
