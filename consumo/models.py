from django.db import models
from apartamento.models import Apartamento
from leitor.models import Leitor
from gas.models import Gas


class Consumo(models.Model):
    id = models.AutoField(primary_key=True)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE)
    leitura = models.DecimalField(max_digits=11, decimal_places=2)
    data_leitura = models.DateField()
    periodo_leitura = models.IntegerField()
    consumo = models.DecimalField(max_digits=11, decimal_places=2)
    gas = models.ForeignKey('gas.Gas', on_delete=models.CASCADE)
    valor_pagamento = models.DecimalField(max_digits=11, decimal_places=2)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    consumo_anterior = models.ForeignKey('self', related_name='consumo_anterior_set', on_delete=models.CASCADE,
                                         null=True, blank=True)

    class Meta:
        db_table = 'consumo'

    def __str__(self):
        string = 'Apartamento: ' + str(self.apartamento) + ' \n' \
            'Data da Leitura: ' + str(self.data_leitura) + ' \n' \
            'Leitura Atual: ' + str(self.leitura) + ' \n' \
            'Consumo Atual: ' + str(self.consumo) + ' \n' \
            'Valor do Gás: R$' + str(self.gas.valor) + ' \n' \
            'Valor a Pagar: R$' + str(self.valor_pagamento)
        return string
