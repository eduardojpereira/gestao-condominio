from rest_framework import serializers

from leitor.models import Leitor


class LeitorResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leitor
        fields = 'identificador'


class LeitorInputSerializer(serializers.Serializer):

    identificador = serializers.CharField(help_text="Identificador do leitor.")
