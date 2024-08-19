from django.urls import path
from . import views

urlpatterns = [
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path('orden/<int:pk>/', views.detalle_orden, name='detalle_orden'),
]
