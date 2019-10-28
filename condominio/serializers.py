from rest_framework import serializers

from condominio.models import Condominio


class CondominioResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condominio
        fields = ('nome', 'cnpj', 'endereco')
