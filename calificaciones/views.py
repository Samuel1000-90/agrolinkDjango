from django.shortcuts import render, redirect
from .models import Calificacion
from productos.models import Producto

def lista_calificaciones(request):
    calificaciones = Calificacion.objects.select_related('producto', 'usuario').all().order_by('-fecha')
    return render(request, "calificaciones/lista.html", {
        "calificaciones": calificaciones
    })


def crear_calificacion(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == "POST":
        puntaje = request.POST.get("puntaje")
        comentario = request.POST.get("comentario")

        Calificacion.objects.create(
            producto=producto,
            usuario=request.user,
            puntaje=puntaje,
            comentario=comentario
        )

        return redirect("lista_productos")

    return render(request, "calificaciones/form.html", {
        "producto": producto
    })