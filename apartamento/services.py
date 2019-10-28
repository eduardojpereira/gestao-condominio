from apartamento.models import Apartamento


class ApartamentoService():

    def find(self):
        return Apartamento.objects.all()
