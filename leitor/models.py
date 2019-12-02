from django.db import models

class Leitor(models.Model):
    id = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=10)
	
    class Meta:
        db_table = 'leitor'

    def __str__(self):
        return 'Identificador: ' + str(self.identificador)
