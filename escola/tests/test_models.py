from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'teste',
            email = 'teste@teste.com',
            cpf = '25297081009',
            data_nascimento = '2025-01-09',
            celular = '86 99999-9999'
        )

    def test_verifica_atributos_de_estudante(self):
        """
        Teste que verifica os atributos do modelo de Estudante
        """
        self.assertEqual(self.estudante.nome, 'teste')
        self.assertEqual(self.estudante.email, 'teste@teste.com')
        self.assertEqual(self.estudante.cpf, '25297081009')
        self.assertEqual(self.estudante.data_nascimento, '2025-01-09')
        self.assertEqual(self.estudante.celular, '86 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'TESTE',
            descricao = 'Curso de teste',
            nivel = 'A',
        )

    def test_verifica_atributos_de_curso(self):
        """
        Teste que verifica os atributos do modelo de Curso
        """
        self.assertEqual(self.curso.codigo, 'TESTE')
        self.assertEqual(self.curso.descricao, 'Curso de teste')
        self.assertEqual(self.curso.nivel, 'A')
        
class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'teste',
            email = 'teste@teste.com',
            cpf = '25297081009',
            data_nascimento = '2025-01-09',
            celular = '86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo = 'TESTE',
            descricao = 'Curso de teste',
            nivel = 'A',
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante_matricula,
            curso = self.curso_matricula,
            periodo = 'M',
        )

    def test_verifica_atributos_de_matricula(self):
        """
        Teste que verifica os atributos do modelo de Matricula
        """
        self.assertEqual(self.matricula.estudante, self.estudante_matricula)
        self.assertEqual(self.matricula.curso, self.curso_matricula)
        self.assertEqual(self.matricula.periodo, 'M')
