from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo.json']
    
    def test_carregamento_da_fixtures(self):
        """"
        Teste que verifica o carregamento da fixtures
        """
        estudante = Estudante.objects.get(cpf='15262065953')
        curso = Curso.objects.get(pk=1)
        self.assertEqual (estudante.celular, "46 94471-8339")
        self.assertEqual(curso.codigo, 'CPOO1')