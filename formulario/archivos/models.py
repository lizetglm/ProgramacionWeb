from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    semestre = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Archivos(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return f"Archivo de {self.estudiante.nombre}"