from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import Sum, F, FloatField

# Create your models here.

class Pedidos(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



    @property
    def total(self):
        # aggregate retornará un diccionario con:
        # {"total": suma total de lo que cuesta el pedido}
        return self.lineapedido_set.aggregate(
            total=Sum(F("producto__precio") * F("cantidad"), output_field=FloatField())
        )["total"]
    

    class Meta():
        db_table = "Pedidos"
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        ordering = ["id"]




class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



    class Meta():
        db_table = "LineaPedido"
        verbose_name_plural = "Lineas de pedido"
        verbose_name = "Linea de pedido"
        ordering = ["id"]

