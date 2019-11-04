from consumo.models import Consumo


class ConsumoService:

    def find(self):
        return Consumo.objects.all()
