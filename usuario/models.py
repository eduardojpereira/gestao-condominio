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

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return 'Nome: ' + str(self.nome) + 'Sobrenome: ' \
               + str(self.sobrenome) + 'Cpf: ' + str(self.cpf) \
               + 'E-mail: ' + str(self.email) + 'Telefone: ' \
               + str(self.telefone) + 'Data de início da moradia: ' \
               + str(self.data_inicio_moradia) + 'Data de término da moradia: ' \
               + str(self.data_fim_moradia) + 'Status: ' + str(self.status)
