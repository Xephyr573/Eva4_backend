from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet, PropiedadViewSet, AgenteViewSet, VisitaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Configuracion de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Gestion de Inmuebles",
        default_version='v1',
        description="Evaluacion 4 de Backend, Proyecto de Gestión de Inmuebles",
        contact=openapi.Contact(email="Mati@mal.com"),
    ),
    public=True,
    permissions_classes=(permission.AllowAny,),
)

router = DefaultRouter()
router.register(r'propietarios', views.PropietarioViewSet)
router.register(r'propiedad', views.PropiedadViewSet)
router.register(r'agente', views.AgenteViewSet)
router.register(r'visitas', views.VisitasViewSet)
