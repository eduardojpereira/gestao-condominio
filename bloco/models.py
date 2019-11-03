from django.db import models


class Bloco(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    condominio = models.ForeignKey('condominio.Condominio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bloco'

    def __str__(self):
        return self.nome
