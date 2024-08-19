from django.urls import path
from . import views

urlpatterns = [
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('factura/<int:pk>/', views.detalle_factura, name='detalle_factura'),
]

