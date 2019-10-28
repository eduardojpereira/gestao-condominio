from rest_framework import serializers

from condominio.models import Condominio


class CondominioResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condominio
        fields = ('id', 'nome', 'cnpj', 'endereco')


class CondominioInputSerializer(serializers.Serializer):

    nome = serializers.CharField(help_text="Nome do Condomínio. Máximo de 255 caracteres")
    endereco = serializers.CharField(help_text="Endereço do Condomínio. Máximo de 255 caracteres")
    cnpj = serializers.CharField(help_text="CNPJ do Condomínio. Máximo de 14 caracteres")
