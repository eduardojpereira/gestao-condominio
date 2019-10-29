from rest_framework import serializers

from usuario.models import Usuario


class UsuarioResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'sobrenome', 'apartamento',
                  'cpf', 'email', 'telefone', 'data_inicio_moradia',
                  'data_fim_moradia', 'status')


class UsuarioInputSerializer(serializers.Serializer):

    nome = serializers.CharField(help_text="Nome do Usuário.")
    sobrenome = serializers.CharField(help_text="Sobrenome do Usuário.")
    apartamento = serializers.CharField(help_text="Apartamento do usuário.")
    cpf = serializers.CharField(help_text="CPF do usuário.")
    email = serializers.CharField(help_text="E-mail do usuário.")
    telefone = serializers.CharField(help_text="Telefone de contato.")
    data_inicio_moradia = serializers.DateField()
    data_fim_moradia = serializers.DateField()
    status = serializers.BooleanField()
