from django.contrib import admin
from .models import Proveedor, OrdenCompra, DetalleOrdenCompra

admin.site.register(Proveedor)
admin.site.register(OrdenCompra)
admin.site.register(DetalleOrdenCompra)
