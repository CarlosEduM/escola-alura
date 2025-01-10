from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')

    def test_authenticacao_com_credenciais_corretas(self):
        """
        Teste de autenticação com credenciais corretas
        """
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)

    def test_authenticacao_com_username_incorreto(self):
        """
        Teste de autenticação com username incorreto
        """
        usuario = authenticate(username='admin1', password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_authenticacao_com_senha_incorreta(self):
        """
        Teste de autenticação com senha incorreta
        """
        usuario = authenticate(username='admin', password='12345')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)

    def test_requisição_get_autorizada(self):
        """
        Teste em uma rota get com usuário autorizado
        """
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisição_get_nao_autorizada(self):
        """
        Teste em uma rota get com usuário não autorizado
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
