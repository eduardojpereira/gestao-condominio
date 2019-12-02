from model_mommy import mommy
from rest_framework import status

from commons.test import CustomAPITestCase
from condominio.serializers import CondominioResponseSerializer
from ..models import Condominio


class TestCondominioAPI(CustomAPITestCase):

    def setUp(self):
        self.path = '/v1/condominios/'

    def _create_condominio_fixtures(self):
        mommy.make('Condominio', id=1, nome='Residencial Línea', cnpj='83172782000173', endereco="Rua passagem")
        mommy.make('Condominio', id=2, nome='Residencial Lírios', cnpj='01720425000138', endereco="Rua leoberto")

    def test_post__success(self):
        nome = 'Condominio A'
        cnpj = '72711425000110'
        endereco = 'Rua virgilino ferreira de souza'

        data = dict(nome=nome, cnpj=cnpj, endereco=endereco)

        response = self.send_post(path=self.path, data=data)

        self.assertResponse(response, status.HTTP_200_OK, 'Condomínio inserido com sucesso')

    def test_put__success(self):
        self._create_condominio_fixtures()

        novos_dados_do_condominio = dict(nome='Condominio B', cnpj='67768505000171', endereco='Rua oliveira')

        condominio_id = 1
        condominio_antes_do_update = Condominio.objects.get(id=condominio_id)
        self.assertNotEqual(novos_dados_do_condominio['nome'], condominio_antes_do_update.nome)
        self.assertNotEqual(novos_dados_do_condominio['cnpj'], condominio_antes_do_update.cnpj)
        self.assertNotEqual(novos_dados_do_condominio['endereco'], condominio_antes_do_update.endereco)

        url = f'{self.path}{condominio_id}/'
        response = self.client.put(path=url, data=novos_dados_do_condominio)

        self.assertResponse(response, status.HTTP_200_OK, 'Condomínio atualizado com sucesso')

        condominio_depois_do_update = Condominio.objects.get(id=condominio_id)
        self.assertEqual(novos_dados_do_condominio['nome'], condominio_depois_do_update.nome)
        self.assertEqual(novos_dados_do_condominio['cnpj'], condominio_depois_do_update.cnpj)
        self.assertEqual(novos_dados_do_condominio['endereco'], condominio_depois_do_update.endereco)

    def test_get__success(self):
        self._create_condominio_fixtures()

        response = self.client.get(self.path)

        obtained_data = response.data

        self.assertTrue(len(obtained_data))
        self.assertEqual(2, len(obtained_data))

        condominios_esperados = Condominio.objects.filter(id__in=[1, 2])
        json_esperado = CondominioResponseSerializer(condominios_esperados, many=True).data
        self.assertEqual(obtained_data, json_esperado)

    def test_get_by_id__success(self):
        self._create_condominio_fixtures()

        condominio_id = 1

        url = f'{self.path}{condominio_id}/'
        response = self.client.get(url)

        self.assertResponse(response, status.HTTP_200_OK)

        obtained = response.data
        self.assertTrue(obtained)

        condominio_esperado = Condominio.objects.get(id=condominio_id)
        json_esperado = CondominioResponseSerializer(condominio_esperado).data
        self.assertEqual(obtained, json_esperado)

    def test_delete__success(self):
        self._create_condominio_fixtures()
        condominio_id = 1

        self.assertTrue(Condominio.objects.filter(id=condominio_id).exists())

        url = f'{self.path}{condominio_id}/'
        response = self.client.delete(url)

        self.assertResponse(response, status.HTTP_200_OK, 'Condomínio deletado com sucesso')

        self.assertFalse(Condominio.objects.filter(id=condominio_id).exists())
