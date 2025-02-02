# products/models.py

from django.db import models
from insumo.models import Insumo

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio base del producto
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Calcula el costo total del producto
    def calculate_total_cost(self):
        total_cost = 0
        for ingredient in self.ingredients.all():
            total_cost += ingredient.calculate_cost()
        return total_cost
    
    def __str__(self):
        return self.name

class ProductInsumo(models.Model):
    product = models.ForeignKey(Product, related_name='ingredients', on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Cantidad del insumo usada
    unit = models.CharField(max_length=20)  # Unidad de medida de esa cantidad (e.g., gramos, kilogramos)

    def calculate_cost(self):
        # Obtener el costo por unidad de insumo (por ejemplo, el costo de un kilogramo de queso)
        if self.unit == 'kg':
            # Si la unidad es kg, usamos el costo por kg
            cost_per_unit = self.insumo.costo
        elif self.unit == 'g':
            # Si la unidad es gramos, convertimos el costo del insumo por kg a costo por gramo
            cost_per_unit = self.insumo.costo / 1000
        else:
            cost_per_unit = self.insumo.costo

        # Calcular el costo total del insumo usado en esta cantidad
        return cost_per_unit * self.quantity

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.insumo.name} for {self.product.name}"
