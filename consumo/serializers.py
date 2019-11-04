from rest_framework import serializers
from consumo.models import Consumo


class ConsumoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ('apartamento', 'data_leitura_atual', 'leitura_atual', 'periodo_leitura',
                  'consumo_atual', 'valor_gas', 'valor_pagamento')
