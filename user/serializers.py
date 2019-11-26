from rest_framework import serializers

from user.models import User


class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('cpf', 'first_name', 'last_name', 'email',
                  'apartamento', 'telephone', 'date_inicio', 'date_final',
                  'status')


class UserInputSerializer(serializers.Serializer):
    cpf = serializers.CharField(help_text="CPF.")
    first_name  = serializers.CharField(help_text="Nome do Usuário.")
    last_name = serializers.CharField(help_text="Sobrenome do Usuário.")
    email = serializers.CharField(help_text="E-mail do usuário.")
    apartamento = serializers.CharField(help_text="Apartamento do usuário.")
    telephone = serializers.CharField(help_text="Telefone de contato.")
    date_inicio = serializers.CharField(help_text='Data entrada ao apartamento.')
    date_final = serializers.CharField(help_text='Data saida do apartamento.', required=False)
