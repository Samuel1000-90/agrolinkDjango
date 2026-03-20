from django.shortcuts import render
from .models import Producto, ProductoFinca,ImagenesProducto 
from pedidos.models import DetallesCompra
from django.db.models import Sum
from django.conf import settings


def inicio(request):
    # Traer productos con finca y productor
    productos_finca = ProductoFinca.objects.select_related(
        'id_finca', 'id_producto', 'id_finca__id_usuario'
    )
    
    


    # Todos los productos
    productos = Producto.objects.all()
    for p in productos:
        p.imagen_principal = p.imagenProducto.filter(es_principal=1).first()



    # Producto más vendido
    producto_destacado = (
        DetallesCompra.objects
        .values('id_producto')  # usar el nombre correcto del campo
        .annotate(total_vendido=Sum('cantidad'))
        .order_by('-total_vendido')
        .first()
    )

    destacado = None
    if producto_destacado:
        destacado = Producto.objects.get(id_producto=producto_destacado['id_producto'])

    return render(request, 'productos/inicio.html', {
        'productos': productos,
        'productos_finca': productos_finca,
        'destacado': destacado,
        "MEDIA_URL": settings.MEDIA_URL

        
    })
    



def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/inicio.html", {"productos": productos})

