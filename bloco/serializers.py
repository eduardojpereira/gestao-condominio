from rest_framework import serializers

from bloco.models import Bloco


class BlocoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = ('id', 'nome')


