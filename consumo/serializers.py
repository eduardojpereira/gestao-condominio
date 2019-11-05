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
