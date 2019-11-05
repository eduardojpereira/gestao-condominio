from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    apartamento = models.ForeignKey('apartamento.Apartamento', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    data_inicio_moradia = models.CharField(max_length=10)
    data_fim_moradia = models.CharField(max_length=10, null=True, blank=True) 
    status = models.BooleanField()
	

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return 'Nome: ' + str(self.nome)