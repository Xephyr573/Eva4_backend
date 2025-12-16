from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Propietario, Agente, Propiedad, Visita
from .serializer import PropietarioSerializer, AgenteSerializer, PropiedadSerializer, VisitaSerializer
from rest_framework.permissions import IsAuthenticated

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [IsAuthenticated]

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer
    permission_classes = [IsAuthenticated]

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtros exactos para comuna y tipo, filtro de rango automático para precio
    filterset_fields = {
        'comuna': ['exact'],
        'tipo_propiedad': ['exact'],
        'precio': ['exact', 'gte', 'lte'],
    }
    search_fields = ['titulo', 'comuna']
    ordering_fields = ['precio', 'comuna']

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha_hora', 'estado']