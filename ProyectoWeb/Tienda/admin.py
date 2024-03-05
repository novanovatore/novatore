from django.contrib import admin
from .models import *
# Register your models here.


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")



class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)