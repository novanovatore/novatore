from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="servicios")
    created = models.DateTimeField(auto_now_add=True) # cuando se creó
    updated = models.DateTimeField(auto_now_add=True) # ultima vez que se actualizo 

    # esto es para configurar los metadatos de la tabla
    class Meta():
        # nombre de la tabla en la base de datos
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
    

    # representación string de la tabla
    def __str__(self):
        return self.titulo