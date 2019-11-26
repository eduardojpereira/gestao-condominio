from django.test import SimpleTestCase

from bloco.models import Bloco


class TestBloco(SimpleTestCase):

    def test_str(self):
        bloco = Bloco(nome='A')

        self.assertEqual(bloco.nome, str(bloco))
