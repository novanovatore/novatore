from django.contrib import admin
from .models import *

# Register your models here.


class PedidosAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)


admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)