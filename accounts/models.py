from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    direccion = models.TextField(blank=True, null=True, verbose_name="Dirección")
    rol = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Administrador'),
            ('usuario', 'Usuario estándar'),
        ],
        default='usuario',
        verbose_name="Rol"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Telefono(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='telefonos')
    numero = models.CharField(max_length=20, verbose_name="Número de teléfono")

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = "Teléfono"
        verbose_name_plural = "Teléfonos"


class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')
    descripcion = models.TextField(verbose_name="Dirección")
    principal = models.BooleanField(default=False, verbose_name="Dirección principal")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class PreferenciasUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='preferencias')
    equipo_futbol = models.CharField(max_length=50, blank=True, null=True, verbose_name="Equipo de fútbol favorito")

    def __str__(self):
        return f"Preferencias de {self.usuario.username}"

    class Meta:
        verbose_name = "Preferencias del Usuario"
        verbose_name_plural = "Preferencias de los Usuarios"