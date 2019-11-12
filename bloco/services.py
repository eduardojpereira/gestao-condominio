from bloco.models import Bloco


class BlocoService:

    def find(self):
        return Bloco.objects.all()