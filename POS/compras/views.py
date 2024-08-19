from django.shortcuts import render, get_object_or_404
from .models import OrdenCompra

def detalle_orden(request, pk):
    orden = get_object_or_404(OrdenCompra, pk=pk)
    return render(request, 'compras/detalle_orden.html', {'orden': orden})
