from django.db import models
from django import forms

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    password = forms.CharField(widget=forms.PasswordInput)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    apartamento = models.ForeignKey('apartamento.Apartamento', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_inicio_moradia = models.DateField()
    data_fim_moradia = models.DateField(null=True, blank=True) 
    status = models.BooleanField()
	

    class Meta:
        db_table = 'usuario'
        model = Usuario

    def __str__(self):
        return 'Nome: ' + str(self.nome)