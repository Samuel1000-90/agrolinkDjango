from django.shortcuts import render, redirect, get_object_or_404
from .models import Calificacion

def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificaciones/lista.html', {
        'calificaciones': calificaciones
    })


def crear_calificacion(request):
    if request.method == 'POST':
        Calificacion.objects.create(
            nombre_referencia=request.POST['nombre'],
            tipo=request.POST['tipo'],
            puntuacion=request.POST['puntuacion'],
            comentario=request.POST['comentario']
        )
        return redirect('lista_calificacion')

    return render(request, 'calificaciones/crear.html')


def editar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)

    if request.method == 'POST':
        calificacion.nombre_referencia = request.POST['nombre']
        calificacion.tipo = request.POST['tipo']
        calificacion.puntuacion = request.POST['puntuacion']
        calificacion.comentario = request.POST['comentario']
        calificacion.save()
        return redirect('lista_calificacion')

    return render(request, 'calificaciones/editar.html', {'calificacion': calificacion})


def eliminar_calificacion(request, id):
    calificacion = get_object_or_404(Calificacion, id=id)
    calificacion.delete()
    return redirect('lista_calificacion')

def base(request):
    return render(request, 'base.html')