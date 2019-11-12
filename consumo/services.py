from datetime import datetime

from rest_framework.exceptions import NotFound
from consumo.models import Consumo
from gas.models import Gas

class ConsumoService:

    def find(self):
        return Consumo.objects.all()

    def insert(self, params):
        consumo_atual = Consumo()
        consumo_atual.apartamento_id = params['apartamento']
        consumo_atual.leitor_id = params['leitor']
        consumo_atual.leitura = params['leitura']
        consumo_atual.data_leitura = params['data_leitura']
        gas = Gas.objects.last()
        valor_gas = gas.valor
        consumo_atual.gas = gas

        consumo_anterior = self._get_consumo_anterior(consumo_atual)
        consumo_atual.periodo_leitura = self._calcular_periodo_leitura(consumo_atual.data_leitura,
                                                                       consumo_anterior.data_leitura)
        consumo_atual.consumo = self._calcular_consumo_atual(consumo_atual.leitura, consumo_anterior.leitura)
        consumo_atual.valor_pagamento = self._calcular_valor_pagamento(consumo_atual.consumo, valor_gas,
                                                                       gas.unidade_conversao)
        consumo_atual.consumo_anterior_id = consumo_anterior.id
        consumo_atual.save()

    def _get_consumo_anterior(self, consumo_atual):
        consumo_anterior = Consumo.objects.filter(apartamento_id=consumo_atual.apartamento_id).order_by('id').last()

        if consumo_anterior:
            return consumo_anterior

        return consumo_atual

    def update(self, params):
        consumo_id = params['id']

        consumo_atual = Consumo.objects.get(id=consumo_id)

        consumo_anterior = consumo_atual.consumo_anterior
        consumo_atual.leitor_id = params['leitor']
        consumo_atual.leitura = params['leitura']
        consumo_atual.data_leitura = params['data_leitura']
        gas = Gas.objects.last()
        consumo_atual.gas = gas
        consumo_atual.periodo_leitura = self._calcular_periodo_leitura(consumo_atual.data_leitura,
                                                                       consumo_anterior.data_leitura)
        consumo_atual.consumo = self._calcular_consumo_atual(consumo_atual.leitura, consumo_anterior.leitura)
        consumo_atual.valor_pagamento = self._calcular_valor_pagamento(consumo_atual.consumo, gas.valor,
                                                                       gas.unidade_conversao)
        consumo_atual.save(update_fields=['leitor', 'leitura', 'data_leitura', 'periodo_leitura',
                                          'valor_pagamento', 'consumo'])

    def delete(self, consumo_id):
        try:
            Consumo.objects.get(id=consumo_id).delete()
        except Consumo.DoesNotExist:
            raise NotFound(detail='Consumo não encontrado')

    def find_by_id(self, consumo_id):
        try:
            return Consumo.objects.get(id=consumo_id)
        except Consumo.DoesNotExist:
            raise NotFound(detail='Consumo não encontado')

    def _calcular_periodo_leitura(self, data_leitura_atual, data_leitura_anterior):
        data_leitura_atual = datetime.strptime(data_leitura_atual, '%Y-%m-%d')
        data_leitura_anterior = datetime.strptime(data_leitura_anterior, '%Y-%m-%d')

        return abs((data_leitura_atual - data_leitura_anterior).days)

    def _calcular_consumo_atual(self, leitura_atual, leitura_anterior):
        return leitura_atual - leitura_anterior

    def _calcular_valor_pagamento(self, consumo, valor_gas, unidade_conversao):
        consumo_em_kg = consumo * unidade_conversao

        return consumo_em_kg * valor_gas
