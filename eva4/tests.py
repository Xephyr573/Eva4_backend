from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Agente

#Create your test here.

class TestModeloAgente(TestCase):
    def test_creacion_agente(self):
        # 1. Crear
        agente = Agente.objects.create(
            nombre="Zack Test",
            numero_licencia="LIC-TEST-2025",
            email="zack.test@example.com"
        )
        # 2. Verificar
        self.assertEqual(agente.nombre, "Zack Test")
        self.assertEqual(agente.numero_licencia, "LIC-TEST-2025")
        self.assertTrue(Agente.objects.filter(numero_licencia="LIC-TEST-2025").exists())

    def test_string_agente(self):
        # Verificar que al imprimir el objeto salga su nombre
        agente = Agente.objects.create(nombre="Agente Bond", email="007@mi6.com")
        self.assertEqual(str(agente), "Agente Bond")

class TestAPIConexion(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = User.objects.create_user(username='tester', password='123')

    def test_api_protegida_sin_login(self):
        # Debe rechazar (401 Unauthorized)
        response = self.client.get('/eva4/agentes/')
        self.assertEqual(response.status_code, 401)

    def test_api_acceso_con_login(self):
        # Logueo
        self.client.force_authenticate(user=self.usuario)
        
        # Debe aceptar (200 OK)
        response = self.client.get('/eva4/agentes/')
        self.assertEqual(response.status_code, 200)