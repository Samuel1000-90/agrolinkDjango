from django.contrib import admin
from .models import Producto, CategoriaProducto, Finca, ProductoFinca, ImagenesProducto

# Registrar modelos simples
admin.site.register(CategoriaProducto)
admin.site.register(ProductoFinca)
admin.site.register(Finca)

# Inline para imágenes
class ImagenesProductoInline(admin.TabularInline):
    model = ImagenesProducto
    extra = 1
    fields = ('url_imagen', 'es_principal')

# Aquí sí va el decorador, sobre la clase ProductoAdmin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'id_usuario')
    inlines = [ImagenesProductoInline]