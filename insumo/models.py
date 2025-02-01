from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    CATEGORIA_CHOICES = [
        ('unidad', 'Unidad'),
        ('peso', 'Peso'),
    ]
    
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=6, choices=CATEGORIA_CHOICES)
    imagen = models.ImageField(upload_to='insumos/', blank=True, null=True)
    descripcion = models.TextField()
    cantidad_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
