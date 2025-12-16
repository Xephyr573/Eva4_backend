from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet, AgenteViewSet, PropiedadViewSet, VisitaViewSet

router = DefaultRouter()
router.register(r'propietarios', PropietarioViewSet)
router.register(r'agentes', AgenteViewSet)
router.register(r'propiedades', PropiedadViewSet)
router.register(r'visitas', VisitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]