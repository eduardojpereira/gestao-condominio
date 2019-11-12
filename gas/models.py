from django.db import models


class Gas(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    unidade_conversao = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = 'gas'

    def __str__(self):
        string = 'Valor do Gás: ' + str(self.valor) + \
            ' Unidade de Conversão(de m³ para kg): ' + str(self.unidade_conversao)
        return string
