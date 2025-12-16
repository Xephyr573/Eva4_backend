from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Propietario, Agente, Propiedad, Visita
from .serializer import PropietarioSerializer, AgenteSerializer, VisitaSerializer, PropiedadSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer
    permission_classes = [IsAuthenticated]

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_hora', 'estado']

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['cimuna', 'tipo_propiedad']
    search_fields = ['titulo', 'comuna']