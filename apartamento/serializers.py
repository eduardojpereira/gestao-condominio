from rest_framework import serializers

from apartamento.models import Apartamento


class ApartamentoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = ('bloco', 'numero', 'esta_disponivel')


class ApartamentoInputSerializer(serializers.Serializer):

    numero = serializers.IntegerField(help_text="Número do Apartamento. Máximo de 11 números")
    esta_disponivel = serializers.BooleanField(help_text="Esse apartamento está disponível? True ou False")
    bloco = serializers.IntegerField(help_text="Id do bloco. Máximo de 11 números")
