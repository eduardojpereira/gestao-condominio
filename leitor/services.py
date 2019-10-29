from .models import Leitor


class LeitorService:

    def find(self):
        return Leitor.objects.all()

    def insert(self, params):
        leitor = Leitor()
        leitor.identificador = params['identificador']

        leitor.save()

        return leitor
