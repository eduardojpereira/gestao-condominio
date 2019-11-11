from rest_framework import serializers
from consumo.models import Consumo


class ConsumoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = ('apartamento',
                  'leitor',
                  'leitura',
                  # 'leitura_anterior',
                  'data_leitura',
                  # 'data_leitura_anterior',
                  'periodo_leitura',
                  'consumo',
                  'valor_gas',
                  'valor_pagamento')


class ConsumoInputSerializer(serializers.Serializer):

    apartamento = serializers.IntegerField(help_text='Id do Apartamento.')
    leitor = serializers.IntegerField(help_text='Id do Responsável pela Leitura.')
    leitura = serializers.DecimalField(max_digits=11, decimal_places=2)
    data_leitura = serializers.DateField(help_text='Data da Leitura.')


class ConsumoUpdateSerializer(serializers.Serializer):

    leitor = serializers.IntegerField(help_text='Id do Responsável pela Leitura.')
    leitura = serializers.DecimalField(max_digits=11, decimal_places=2)
    data_leitura = serializers.DateField(help_text='Data da Leitura.')
