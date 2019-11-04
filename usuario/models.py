from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_inicio_moradia = models.DateField()
    data_fim_moradia = models.DateField()
    status = models.BooleanField()
	apartamento = models.ForeignKey('apartamento.Apartamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return 'Nome: ' + str(self.nome)