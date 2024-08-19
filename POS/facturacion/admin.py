from django.contrib import admin
from .models import Cliente, Factura, DetalleFactura

admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
