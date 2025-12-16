from rest_framework import serializers
from .models import Propietario, Agente, Propiedad, Visita
from django.utils import timezone

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = '__all__'

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

#Validacion extra
def validate_fecha_hora(self, value):
    if value < timezone.now():
        raise serializers.ValidationError("No se pueden agregar visitas en el pasado")
    return value