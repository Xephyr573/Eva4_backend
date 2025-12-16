from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Agente(models.Model):
    nombre = models.CharField(max_length=100)
    numero_licencia = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Propiedad(models.Model):
    TIPO_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPTO', 'Departamento'),
        ('TERRENO', 'Terreno'),
        ('OFICINA', 'Oficina')
    ]

    titulo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100) 
    precio = models.DecimalField(max_digits=12, decimal_places=2) 
    tipo_propiedad = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True)
    
    # Relaciones
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='propiedades')
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, related_name='propiedades_asignadas')

    def __str__(self):
        return f"{self.titulo} ({self.comuna})"

class Visita(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='visitas')
    nombre_interesado = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, default='PENDIENTE')

    # Validación de fecha requerida 
    def clean(self):
        if self.fecha_hora < timezone.now():
            raise ValidationError("La fecha de la visita no puede ser en el pasado.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Visita a {self.propiedad} - {self.fecha_hora}"