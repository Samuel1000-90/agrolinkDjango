from django.db import models    
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    
    @property
    def id(self):
        return self.id_calificacion

    class Meta:
        managed = False
        db_table = 'tb_calificacion'