from django.test import SimpleTestCase

from condominio.models import Condominio


class TestCondominio(SimpleTestCase):

    def test_str(self):
        nome = 'Residencial Línea'
        condominio = Condominio(nome=nome)

        self.assertEqual(nome, str(condominio))
