from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User

class Calificacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="calificaciones")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.producto} ({self.puntaje})"