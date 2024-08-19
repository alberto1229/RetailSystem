from django.shortcuts import render, get_object_or_404
from .models import Factura

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturacion/lista_facturas.html', {'facturas': facturas})

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    return render(request, 'facturacion/detalle_factura.html', {'factura': factura})
