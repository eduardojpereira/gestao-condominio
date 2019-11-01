from django.db import models
from apartamento.models import Apartamento

# Create your models here.
class Consumo(models.Model):

    id = models.AutoField(primary_key=True) #
    apartamento = Apartamento #
    data_leitura_atual = models.DateField() #
    leitura_atual = models.FloatField() #
    data_leitura_anterior = ''
    periodo_leitura = '' #
    consumo_atual = 0 #
    valor_gas = models.FloatField() #
    valor_pagamento = '' #

    class Meta:
        db_table = 'consumo'

    def __str__(self):
        string = 'Apartamento: ' + str(self.apartamento) + '\n' \
                    'Data da Leitura: ' + str(self.data_leitura_atual) + '\n' \
                     'Leitura Atual: ' + str(self.data_leitura_atual) + 'm³ \n' \
                     'Período da Leitura: ' + str(self.periodo_leitura) + '\n' \
                     'Consumo Atual: ' + str(self.consumo_atual) + '\n' \
                     'Valor do Gás: R$' + str(self.valor_gas) + '/kg \n' \
                     'Valor a Pagar: R$' + str(self.valor_gas) + '\n'
        return string