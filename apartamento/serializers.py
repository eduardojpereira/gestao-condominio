from rest_framework import serializers

from apartamento.models import Apartamento


class ApartamentoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = ('id', 'bloco', 'numero')
