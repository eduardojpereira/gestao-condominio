from model_mommy import mommy
from rest_framework import status

from bloco.serializers import BlocoResponseSerializer
from commons.test import CustomAPITestCase
from ..models import Bloco


class TestBlocoAPI(CustomAPITestCase):

    def setUp(self):
        self.path = '/v1/blocos/'

    def _create_bloco_fixtures(self):
        mommy.make('Condominio', id=1, nome='Residencial Línea', cnpj='83172782000173', endereco="Rua passagem")
        mommy.make('Condominio', id=2, nome='Residencial Lírios', cnpj='01720425000138', endereco="Rua leoberto")

        mommy.make('Bloco', id=1, nome='Bloco 1', condominio_id=1)
        mommy.make('Bloco', id=2, nome='Bloco 2', condominio_id=2)

    def test_post__success(self):
        self._create_bloco_fixtures()

        data = dict(nome='bloco 3', condominio=1)

        response = self.send_post(path=self.path, data=data)

        self.assertResponse(response, status.HTTP_200_OK, 'Bloco inserido com sucesso')

    def test_put__success(self):
        self._create_bloco_fixtures()

        novos_dados_do_bloco = dict(nome='bloco 3', condominio=2)

        bloco_id = 1
        bloco_antes_do_update = Bloco.objects.get(id=bloco_id)
        self.assertNotEqual(novos_dados_do_bloco['nome'], bloco_antes_do_update.nome)
        self.assertNotEqual(novos_dados_do_bloco['condominio'], bloco_antes_do_update.condominio_id)

        url = f'{self.path}{bloco_id}/'
        response = self.client.put(path=url, data=novos_dados_do_bloco)

        self.assertResponse(response, status.HTTP_200_OK, 'Bloco atualizado com sucesso')

        bloco_depois_do_update = Bloco.objects.get(id=bloco_id)
        self.assertEqual(novos_dados_do_bloco['nome'], bloco_depois_do_update.nome)
        self.assertEqual(novos_dados_do_bloco['condominio'], bloco_depois_do_update.condominio_id)

    def test_get__success(self):
        self._create_bloco_fixtures()

        response = self.client.get(self.path)

        obtained_data = response.data

        self.assertTrue(len(obtained_data))
        self.assertEqual(2, len(obtained_data))

        blocos_esperados = Bloco.objects.filter(id__in=[1, 2])
        json_esperado = BlocoResponseSerializer(blocos_esperados, many=True).data
        self.assertEqual(obtained_data, json_esperado)

    def test_get_by_id__success(self):
        self._create_bloco_fixtures()

        bloco_id = 1

        url = f'{self.path}{bloco_id}/'
        response = self.client.get(url)

        self.assertResponse(response, status.HTTP_200_OK)

        obtained = response.data
        self.assertTrue(obtained)

        bloco_esperado = Bloco.objects.get(id=bloco_id)
        json_esperado = BlocoResponseSerializer(bloco_esperado).data
        self.assertEqual(obtained, json_esperado)

    def test_delete__success(self):
        self._create_bloco_fixtures()

        bloco_id = 1
        self.assertTrue(Bloco.objects.filter(id=bloco_id).exists())

        url = f'{self.path}{bloco_id}/'
        response = self.client.delete(url)

        self.assertResponse(response, status.HTTP_200_OK, 'Bloco deletado com sucesso')

        self.assertFalse(Bloco.objects.filter(id=bloco_id).exists())
