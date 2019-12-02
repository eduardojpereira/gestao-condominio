from django.test import SimpleTestCase

from apartamento.models import Apartamento
from bloco.models import Bloco


class TestApartamento(SimpleTestCase):

    def test_str(self):
        bloco = Bloco(nome='Residencial Línea')
        apartamento = Apartamento(numero=206, bloco=bloco)

        representacao_apartamento = 'Bloco: ' + str(bloco) + ' Número: ' + str(apartamento.numero)
        self.assertEqual(representacao_apartamento, str(apartamento))
