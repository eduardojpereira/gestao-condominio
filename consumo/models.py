from django.db import models
from apartamento.models import Apartamento
from datetime import datetime


class Consumo(models.Model):

    id = models.AutoField(primary_key=True)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    leitura_atual = models.DecimalField(max_digits=11, decimal_places=2)
    leitura_anterior = models.DecimalField(max_digits=11, decimal_places=2)
    data_leitura_atual = models.DateField()
    data_leitura_anterior = models.DateField()
    consumo_atual = models.DecimalField(max_digits=11, decimal_places=2)
    valor_gas = models.DecimalField(max_digits=11, decimal_places=2)
    valor_pagamento = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'consumo'

    def __str__(self):
        string = 'Apartamento: ' + str(self.apartamento) + '\n' \
                    'Data da Leitura: ' + str(self.data_leitura_atual) + '\n' \
                     'Leitura Atual: ' + str(self.leitura_atual) + 'm³ \n' \
                     'Consumo Atual: ' + str(self.consumo_atual) + '\n' \
                     'Valor do Gás: R$' + str(self.valor_gas) + '/kg \n' \
                     'Valor a Pagar: R$' + str(self.valor_gas) + '\n'
        return string

    def _periodo_leitura(self):
        data_leitura_atual = datetime.strptime(self.data_leitura_atual, '%d-%m-%Y')
        data_leitura_anterior = datetime.strptime(self.data_leitura_anterior, '%d-%m-%Y')
        return abs((data_leitura_atual - data_leitura_anterior).days)

    def _consumo_atual(self):
        leitura_atual = self.leitura_atual
        leitura_anterior = self.leitura_anterior
        consumo = leitura_atual - leitura_anterior
        return consumo

    def _valor_pagamento(self):
        consumo_atual = self.consumo_atual
        valor_gas = self.valor_gas
        unidade_conversao = 2.3
        consumo_em_kg = consumo_atual * unidade_conversao
        valor_pagamento = consumo_em_kg * valor_gas
        return valor_pagamento
