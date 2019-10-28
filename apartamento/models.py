from django.db import models

class Apartamento(models.Model):

    id = models.AutoField(primary_key=True)
    bloco = models.IntegerField()
    numero = models.IntegerField()

    class Meta:
        db_table = 'apartamento'

    def __str__(self):
        return 'Bloco: ' + str(self.bloco) + ' Número: ' + str(self.numero)
