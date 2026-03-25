from django.db import models

# Create your models here.
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    puntaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    promedio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_calificacion'

class Calificacion(models.Model):
    tipo = models.CharField(max_length=100)
    puntuacion = models.IntegerField()
    nombre_referencia = models.CharField(max_length=100)

    TIPO_USUARIO = [
        ('vendedor', 'Vendedor'),
        ('transportista', 'Transportista'),
        ('producto', 'Producto'),
    ]


    def __str__(self):
        return f"{self.tipo} - {self.nombre_referencia} ({self.puntuacion})"
