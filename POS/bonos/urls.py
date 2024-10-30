from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bonos, name='lista_bonos'),
    path('bono/<int:bono_id>/', views.detalle_bono, name='detalle_bono'),
    path('crear/', views.crear_bono, name='crear_bono'),
    path('editar/<int:bono_id>/', views.editar_bono, name='editar_bono'),
    path('eliminar/<int:bono_id>/', views.eliminar_bono, name='eliminar_bono'),
]