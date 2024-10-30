from django.shortcuts import render, get_object_or_404, redirect
from .models import Bono
from .forms import BonoForm  # Asegúrate de tener un formulario definido en forms.py

# Vista para listar todos los bonos
def lista_bonos(request):
    bonos = Bono.objects.all()  # Obtener todos los bonos
    return render(request, 'bonos/lista_bonos.html', {'bonos': bonos})

# Vista para ver detalles de un bono específico
def detalle_bono(request, bono_id):
    bono = get_object_or_404(Bono, id=bono_id)  # Obtener el bono o mostrar 404
    return render(request, 'bonos/detalle_bono.html', {'bono': bono})

# Vista para crear un nuevo bono
def crear_bono(request):
    if request.method == 'POST':
        form = BonoForm(request.POST)  # Crear formulario con los datos POST
        if form.is_valid():  # Validar el formulario
            form.save()  # Guardar el nuevo bono en la base de datos
            return redirect('lista_bonos')  # Redirigir a la lista de bonos
    else:
        form = BonoForm()  # Mostrar formulario vacío
    return render(request, 'bonos/crear_bono.html', {'form': form})

# Vista para editar un bono existente
def editar_bono(request, bono_id):
    bono = get_object_or_404(Bono, id=bono_id)  # Obtener el bono a editar
    if request.method == 'POST':
        form = BonoForm(request.POST, instance=bono)  # Crear formulario con los datos del bono
        if form.is_valid():  # Validar el formulario
            form.save()  # Guardar los cambios
            return redirect('detalle_bono', bono_id=bono.id)  # Redirigir a los detalles del bono
    else:
        form = BonoForm(instance=bono)  # Mostrar formulario con datos del bono
    return render(request, 'bonos/editar_bono.html', {'form': form, 'bono': bono})

# Vista para eliminar un bono
def eliminar_bono(request, bono_id):
    bono = get_object_or_404(Bono, id=bono_id)  # Obtener el bono a eliminar
    if request.method == 'POST':
        bono.delete()  # Eliminar bono de la base de datos
        return redirect('lista_bonos')  # Redirigir a la lista de bonos
    return render(request, 'bonos/eliminar_bono.html', {'bono': bono})
