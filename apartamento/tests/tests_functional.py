from model_mommy import mommy
from rest_framework import status

from apartamento.serializers import ApartamentoResponseSerializer
from commons.test import CustomAPITestCase
from ..models import Apartamento


class TestApartamentoAPI(CustomAPITestCase):

    def setUp(self):
        self.path = '/v1/apartamentos/'

    def _create_apartamento_fixtures(self):
        mommy.make('Condominio', id=1, nome='Residencial Línea', cnpj='83172782000173', endereco="Rua passagem")
        mommy.make('Condominio', id=2, nome='Residencial Lírios', cnpj='01720425000138', endereco="Rua leoberto")

        mommy.make('Bloco', id=1, nome='Bloco 1', condominio_id=1)
        mommy.make('Bloco', id=2, nome='Bloco 1', condominio_id=2)

        mommy.make('Apartamento', id=1, numero=1, bloco_id=1)
        mommy.make('Apartamento', id=2, numero=2, bloco_id=2)

    def test_post__success(self):
        self._create_apartamento_fixtures()

        data = dict(numero=206, esta_disponivel=True, bloco=1)

        response = self.send_post(path=self.path, data=data)

        self.assertResponse(response, status.HTTP_200_OK, 'Apartamento inserido com sucesso')

    def test_put__success(self):
        self._create_apartamento_fixtures()

        novos_dados_do_apartamento = dict(numero=206, esta_disponivel=True, bloco=2)

        apartamento_id = 1
        apartamento_antes_do_update = Apartamento.objects.get(id=apartamento_id)
        self.assertNotEqual(novos_dados_do_apartamento['numero'], apartamento_antes_do_update.numero)
        self.assertNotEqual(novos_dados_do_apartamento['esta_disponivel'], apartamento_antes_do_update.esta_disponivel)
        self.assertNotEqual(novos_dados_do_apartamento['bloco'], apartamento_antes_do_update.bloco_id)

        url = f'{self.path}{apartamento_id}/'
        response = self.client.put(path=url, data=novos_dados_do_apartamento)

        self.assertResponse(response, status.HTTP_200_OK, 'Apartamento atualizado com sucesso')

        apartamento_depois_do_update = Apartamento.objects.get(id=apartamento_id)
        self.assertEqual(novos_dados_do_apartamento['numero'], apartamento_depois_do_update.numero)
        self.assertEqual(novos_dados_do_apartamento['esta_disponivel'], apartamento_depois_do_update.esta_disponivel)
        self.assertEqual(novos_dados_do_apartamento['bloco'], apartamento_depois_do_update.bloco_id)

    def test_get__success(self):
        self._create_apartamento_fixtures()

        response = self.client.get(self.path)

        obtained_data = response.data

        self.assertTrue(len(obtained_data))
        self.assertEqual(2, len(obtained_data))

        apartamentos_esperados = Apartamento.objects.filter(id__in=[1, 2])
        json_esperado = ApartamentoResponseSerializer(apartamentos_esperados, many=True).data
        self.assertEqual(obtained_data, json_esperado)

    def test_get_by_id__success(self):
        self._create_apartamento_fixtures()

        apartamento_id = 1

        url = f'{self.path}{apartamento_id}/'
        response = self.client.get(url)

        self.assertResponse(response, status.HTTP_200_OK)

        obtained = response.data
        self.assertTrue(obtained)

        apartamento_esperado = Apartamento.objects.get(id=apartamento_id)
        json_esperado = ApartamentoResponseSerializer(apartamento_esperado).data
        self.assertEqual(obtained, json_esperado)

    def test_delete__success(self):
        self._create_apartamento_fixtures()

        apartamento_id = 1
        self.assertTrue(Apartamento.objects.filter(id=apartamento_id).exists())

        url = f'{self.path}{apartamento_id}/'
        response = self.client.delete(url)

        self.assertResponse(response, status.HTTP_200_OK, 'Apartamento deletado com sucesso')

        self.assertFalse(Apartamento.objects.filter(id=apartamento_id).exists())
