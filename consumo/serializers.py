from rest_framework import serializers

from consumo.models import Consumo


class ConsumoAnteriorResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumo
        fields = ('leitura',
                  'data_leitura',
                  'periodo_leitura',
                  'consumo',
                  'valor_gas',
                  'valor_pagamento')


class ConsumoResponseSerializer(serializers.ModelSerializer):
    consumo_anterior = ConsumoAnteriorResponseSerializer()

    class Meta:
        model = Consumo
        fields = ('apartamento',
                  'leitor',
                  'leitura',
                  'consumo_anterior',
                  'data_leitura',
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
