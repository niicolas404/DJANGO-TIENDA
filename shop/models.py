from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_creacion = models.DateTimeField()

    def __str__(self) -> str:
        return self.nombre