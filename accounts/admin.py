from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Telefono, Direccion, PreferenciasUsuario

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'numero')
    search_fields = ('numero', 'usuario__username')  
    list_filter = ('usuario',)  

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'descripcion', 'principal')  
    search_fields = ('descripcion', 'usuario__username')  
    list_filter = ('usuario', 'principal') 

@admin.register(PreferenciasUsuario)
class PreferenciasUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'equipo_futbol') 
    search_fields = ('equipo_futbol', 'usuario__username')  
    list_filter = ('equipo_futbol',)  

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 1  

class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1

class PreferenciasUsuarioInline(admin.StackedInline):
    model = PreferenciasUsuario
    can_delete = False 

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Campos que se muestran en la lista de usuarios
    list_display = ('username', 'email', 'rol', 'get_equipo_futbol')
    list_filter = ('rol',)  

    # Campos que se muestran en el formulario de creación/edición de usuarios
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'rol')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'rol'),
        }),
    )

    # Inlines
    inlines = [TelefonoInline, DireccionInline, PreferenciasUsuarioInline]

    # Método personalizado para mostrar el equipo de fútbol
    def get_equipo_futbol(self, obj):
        if hasattr(obj, 'preferencias'):
            return obj.preferencias.equipo_futbol
        return "No especificado"
    get_equipo_futbol.short_description = 'Equipo de fútbol'