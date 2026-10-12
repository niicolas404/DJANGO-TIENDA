from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    imagen_url = models.URLField('URL de imagen', blank=True, help_text='Pega una URL pública de la imagen del producto.')
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_creacion = models.DateTimeField()

    def __str__(self) -> str:
        return self.nombre

    @property
    def precio_formateado(self):
        return f"${self.precio:,.0f}".replace(',', '.')