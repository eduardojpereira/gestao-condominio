from model_mommy import mommy
from rest_framework import status

from commons.test import CustomAPITestCase
from consumo.serializers import ConsumoResponseSerializer
from ..models import Consumo


class TestConsumoAPI(CustomAPITestCase):

    def setUp(self):
        self.path = '/v1/consumo/'

    def _create_consumo_fixtures(self):
        mommy.make('Condominio', id=1, nome='Residencial Línea', cnpj='83172782000173', endereco="Rua passagem")
        mommy.make('Bloco', id=1, nome='A', condominio_id=1)
        mommy.make('Apartamento', id=1, bloco_id=1, numero='304', esta_disponivel=False)
        mommy.make('Leitor', id=1, identificador='Ronaldo')
        mommy.make('Consumo', id=1, apartamento_id=1, leitura=10, data_leitura='01/10/2019', periodo_leitura=0,
                   consumo=10, valor_gas=5, valor_pagamento=50, leitor_id=1, consumo_anterior_id=None)

    def test_post__success(self):
        apartamento_id = 1
        leitura = 20
        data_leitura = '01/11/2019'
        periodo_leitura = 30
        consumo = 10
        valor_gas = 5
        valor_pagamento = 50
        leitor_id = 1
        consumo_anterior_id = 1

        data = {'apartamento_id': apartamento_id,
                'leitura': leitura,
                'data_leitura': data_leitura,
                'periodo_leitura': periodo_leitura,
                'consumo': consumo,
                'valor_gas': valor_gas,
                'valor_pagamento': valor_pagamento,
                'leitor_id': leitor_id,
                'consumo_anterior_id': consumo_anterior_id}

        response = self.send_post(path=self.path, data=data)

        self.assertResponse(response, status.HTTP_200_OK, 'Consumo inserido com sucesso')

    def test_put__success(self):
        self._create_consumo_fixtures()

        novos_dados_do_consumo = {'apartamento_id': 1,
                'leitura': 20,
                'data_leitura': '01/11/2019',
                'periodo_leitura': 31,
                'consumo': 11,
                'valor_gas': 5,
                'valor_pagamento': 55,
                'leitor_id': 1,
                'consumo_anterior_id': 1}

        consumo_id = 2
        consumo_antes_do_update = Consumo.objects.get(id=consumo_id)
        self.assertNotEqual(novos_dados_do_consumo['apartamento_id'], consumo_antes_do_update.apartamento_id)
        self.assertNotEqual(novos_dados_do_consumo['leitura'], consumo_antes_do_update.leitura)
        self.assertNotEqual(novos_dados_do_consumo['data_leitura'], consumo_antes_do_update.data_leitura)
        self.assertNotEqual(novos_dados_do_consumo['periodo_leitura'], consumo_antes_do_update.periodo_leitura)
        self.assertNotEqual(novos_dados_do_consumo['consumo'], consumo_antes_do_update.consumo)
        self.assertNotEqual(novos_dados_do_consumo['valor_gas'], consumo_antes_do_update.valor_gas)
        self.assertNotEqual(novos_dados_do_consumo['valor_pagamento'], consumo_antes_do_update.valor_pagamento)
        self.assertNotEqual(novos_dados_do_consumo['leitor_id'], consumo_antes_do_update.leitor_id)
        self.assertNotEqual(novos_dados_do_consumo['consumo_anterior_id'], consumo_antes_do_update.consumo_anterior_id)

        url = f'{self.path}{consumo_id}/'
        response = self.client.put(path=url, data=novos_dados_do_consumo)

        self.assertResponse(response, status.HTTP_200_OK, 'Consumo atualizado com sucesso')

        consumo_depois_do_update = Consumo.objects.get(id=consumo_id)
        self.assertEqual(novos_dados_do_consumo['apartamento_id'], consumo_depois_do_update.apartamento_id)
        self.assertEqual(novos_dados_do_consumo['leitura'], consumo_depois_do_update.leitura)
        self.assertEqual(novos_dados_do_consumo['data_leitura'], consumo_depois_do_update.data_leitura)
        self.assertEqual(novos_dados_do_consumo['periodo_leitura'], consumo_depois_do_update.periodo_leitura)
        self.assertEqual(novos_dados_do_consumo['consumo'], consumo_depois_do_update.consumo)
        self.assertEqual(novos_dados_do_consumo['valor_gas'], consumo_depois_do_update.valor_gas)
        self.assertEqual(novos_dados_do_consumo['valor_pagamento'], consumo_depois_do_update.valor_pagamento)
        self.assertEqual(novos_dados_do_consumo['leitor_id'], consumo_depois_do_update.leitor_id)
        self.assertEqual(novos_dados_do_consumo['consumo_anterior_id'], consumo_depois_do_update.consumo_anterior_id)

    def test_get__success(self):
        self._create_consumo_fixtures()

        response = self.client.get(self.path)

        obtained_data = response.data

        self.assertTrue(len(obtained_data))
        self.assertEqual(2, len(obtained_data))

        consumos_esperados = Consumo.objects.filter(id__in=[1, 2])
        json_esperado = ConsumoResponseSerializer(consumos_esperados, many=True).data
        self.assertEqual(obtained_data, json_esperado)

    def test_get_by_id__success(self):
        self._create_consumo_fixtures()

        consumo_id = 1

        url = f'{self.path}{consumo_id}/'
        response = self.client.get(url)

        self.assertResponse(response, status.HTTP_200_OK)

        obtained = response.data
        self.assertTrue(obtained)

        consumo_esperado = Consumo.objects.get(id=consumo_id)
        json_esperado = ConsumoResponseSerializer(consumo_esperado).data
        self.assertEqual(obtained, json_esperado)

    def test_delete__success(self):
        self._create_consumo_fixtures()
        consumo_id = 2

        self.assertTrue(Consumo.objects.filter(id=consumo_id).exists())

        url = f'{self.path}{consumo_id}/'
        response = self.client.delete(url)

        self.assertResponse(response, status.HTTP_200_OK, 'Consumo deletado com sucesso')

        self.assertFalse(Consumo.objects.filter(id=consumo_id).exists())
