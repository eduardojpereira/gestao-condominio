from bloco.models import Bloco


class BlocoService:

    def find(self):
        return Bloco.objects.all()

    def insert(self, params):
        bloco = Bloco()
        bloco.nome = params['nome']

        bloco.save()