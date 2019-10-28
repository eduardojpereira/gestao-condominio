from .models import Condominio


class CondominioService:

    def find(self):
        return Condominio.objects.all()
