from django.shortcuts import render, redirect
from .forms import InsumoForm

#----------------------------------------------------------------------------------------------------------

def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo insumo en la base de datos
            return redirect('insumos:lista_insumos')  # Redirige a la lista de insumos después de agregar uno
    else:
        form = InsumoForm()

    return render(request, 'insumos/agregar_insumo.html', {'form': form})
