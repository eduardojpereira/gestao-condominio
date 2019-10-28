from django.db import models


class Condominio(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=255)

    class Meta:
        db_table = 'condominio'

    def __str__(self):
        return self.nome
