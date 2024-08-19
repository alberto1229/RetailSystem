from django.db import models

class Cuenta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('pasivo', 'Pasivo'), ('capital', 'Capital')])
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Transaccion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transacción {self.id} - {self.cuenta.nombre}"
