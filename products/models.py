from django.db import models
from insumo.models import Insumo

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Insumo, through='ProductoInsumo')
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_costo(self):
        total = sum(ingreso.costo_total() for ingreso in self.productoinsumo_set.all())
        self.costo = total
        self.save()
        return total

    def __str__(self):
        return self.nombre

class ProductoInsumo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)  # Ej: 400 gramos

    def costo_total(self):
        """
        Calcula el costo total basado en la cantidad utilizada y la unidad de medida del insumo.
        Si el insumo es por peso, se divide la cantidad entre 1000 para convertir de gramos a kg.
        Si el insumo es por unidad, se multiplica por el costo unitario.
        """
        if self.insumo.tipo == 'peso':
            return (self.cantidad / 1000) * self.insumo.costo
        return self.cantidad * self.insumo.costo

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}{self.insumo.unidad_medida} de {self.insumo.nombre}"
