import os
import django
import random
from faker import Faker
from django.utils import timezone

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')
django.setup()

from eva4.models import Agente, Propietario, Propiedad, Visita

fake = Faker('es_CL')

def poblar():
    print("Limpiando datos antiguos... (Opcional)")
    # Visita.objects.all().delete()
    # Propiedad.objects.all().delete()
    # Agente.objects.all().delete()
    # Propietario.objects.all().delete()

    print("Creando Agentes y Propietarios...")
    agentes = []
    for _ in range(5):
        agente = Agente.objects.create(
            nombre=fake.name(),
            numero_licencia=fake.unique.bothify(text='LIC-####'),
            email=fake.unique.email()
        )
        agentes.append(agente)

    propietarios = []
    for _ in range(5):
        prop = Propietario.objects.create(
            nombre=fake.name(),
            email=fake.unique.email(),
            telefono=fake.phone_number()
        )
        propietarios.append(prop)

    print("Creando Propiedades...")
    tipos = ['CASA', 'DEPTO', 'TERRENO', 'OFICINA']
    propiedades = []
    for _ in range(10):
        p = Propiedad.objects.create(
            titulo=f"{random.choice(['Hermosa', 'Gran', 'Acogedora'])} {fake.street_name()}",
            direccion=fake.address(),
            comuna=fake.city(),
            precio=random.randint(50000000, 350000000),
            tipo_propiedad=random.choice(tipos),
            descripcion=fake.text(),
            propietario=random.choice(propietarios),
            agente=random.choice(agentes)
        )
        propiedades.append(p)

    print("Creando Visitas...")
    for _ in range(15):
        fecha_naive = fake.future_datetime(end_date="+30d")
        fecha_aware = timezone.make_aware(fecha_naive)
        
        Visita.objects.create(
            propiedad=random.choice(propiedades),
            nombre_interesado=fake.name(),
            fecha_hora=fecha_aware,
            estado=random.choice(['PENDIENTE', 'APROBADA', 'CANCELADA'])
        )

    print("¡Listo! Base de datos poblada con éxito.")

if __name__ == '__main__':
    poblar()