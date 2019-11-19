from django.test import SimpleTestCase

from consumo.models import Consumo


class TestConsumo(SimpleTestCase):

    def test_str(self):
        apartamento_id = 1
        leitura = 20
        data_leitura = '01/11/2019'
        periodo_leitura = 30
        consumo = 10
        valor_gas = 5
        valor_pagamento = 50
        leitor_id = 1
        consumo_anterior_id = 1

        consumo = Consumo(
            apartamento_id=apartamento_id,
            leitura=leitura,
            data_leitura=data_leitura,
            periodo_leitura=periodo_leitura,
            consumo=consumo,
            valor_gas=valor_gas,
            valor_pagamento=valor_pagamento,
            leitor_id=leitor_id,
            consumo_anterior_id=consumo_anterior_id)

        toString = 'Apartamento: ' + str(apartamento) + ' \n' \
                    'Data da Leitura: ' + str(data_leitura) + ' \n' \
                    'Leitura Atual: ' + str(leitura) + ' \n' \
                    'Consumo Atual: ' + str(consumo) + ' \n' \
                    'Valor do Gás: R$' + str(valor_gas) + ' \n' \
                    'Valor a Pagar: R$' + str(valor_pagamento)

        self.assertEqual(toString, str(consumo))
