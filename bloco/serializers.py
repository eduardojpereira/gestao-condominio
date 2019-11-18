from rest_framework import serializers

from bloco.models import Bloco


class BlocoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = ('id', 'nome')


class BlocoInputSerializer(serializers.Serializer):
    nome = serializers.CharField(help_text='Nome do Bloco.')

