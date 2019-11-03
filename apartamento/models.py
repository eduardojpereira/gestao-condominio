from django.db import models

from bloco.models import Bloco


class Apartamento(models.Model):

    id = models.AutoField(primary_key=True)
    bloco = models.ForeignKey('bloco.Bloco', on_delete=models.CASCADE)
    numero = models.IntegerField()
    esta_disponivel = models.BooleanField(default=False)

    class Meta:
        db_table = 'apartamento'

    def __str__(self):
        return 'Bloco: ' + str(self.bloco) + ' Número: ' + str(self.numero)
