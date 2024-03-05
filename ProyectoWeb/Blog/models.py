from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) # cuando se creó
    updated = models.DateTimeField(auto_now_add=True) # ultima vez que se actualizo 

    # esto es para configurar los metadatos de la tabla
    class Meta():
        # nombre de la tabla en la base de datos
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    

    # representación string de la tabla
    def __str__(self):
        return self.nombre



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True)

    # cuando se borre un usuario, se eliminen todos los post
    # que escribió, o sea, una eliminación en cascada.
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # un post puede pertenecer a más de una categoría y una
    # categoría puede contener a muchos post.
    # Es una relación N a N.
    categoria = models.ManyToManyField(Categoria)

    created = models.DateTimeField(auto_now_add=True) # cuando se creó
    updated = models.DateTimeField(auto_now_add=True) # ultima vez que se actualizo 

    # esto es para configurar los metadatos de la tabla
    class Meta():
        # nombre de la tabla en la base de datos
        verbose_name = "post"
        verbose_name_plural = "posts"
    

    # representación string de la tabla
    def __str__(self):
        return self.titulo
