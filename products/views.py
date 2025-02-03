from django.shortcuts import render, redirect
from .models import Producto, ProductoInsumo
from insumo.models import Insumo
from .forms import ProductoForm, ProductoInsumoFormSet

def create_product(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        formset = ProductoInsumoFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            producto = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.producto = producto
                instance.save()

            producto.calcular_costo()  # Recalcular costo total
            return redirect('admin_dashboard')  # Redirigir al dashboard

    else:
        form = ProductoForm()
        formset = ProductoInsumoFormSet()

    return render(request, 'products/create_product.html', {'form': form, 'formset': formset})
