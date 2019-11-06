from rest_framework import serializers
from consumo.models import Consumo


class ConsumoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ('apartamento',
                  'leitor',
                  'leitura_atual',
                  'leitura_anterior',
                  'data_leitura_atual',
                  'data_leitura_anterior',
                  'periodo_leitura',
                  'consumo_atual',
                  'valor_gas',
                  'valor_pagamento')


class ConsumoInputSerializer:

    apartamento = serializers.CharField(help_text='Número do Apartamento.')
    leitor = serializers.CharField(help_text='Identificação do Responsável pela Leitura.')
    leitura_atual = serializers.DecimalField(max_digits=11, decimal_places=2)
    data_leitura_atual = serializers.DateField(help_text='Data da Leitura.')
