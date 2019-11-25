from rest_framework.exceptions import NotFound

from bloco.models import Bloco


class BlocoService:

    def find(self):
        return Bloco.objects.all()

    def insert(self, params):
        bloco = Bloco()
        bloco.nome = params['nome']
        bloco.condominio_id = params['condominio']

        bloco.save()

    def update(self, params):
        bloco_id = params['id']
        nome = params['nome']
        condominio_id = params['condominio']

        bloco = Bloco(id=bloco_id, nome=nome, condominio_id=condominio_id)

        bloco.save(update_fields=['condominio_id', 'nome'])

    def delete(self, bloco_id):
        try:
            Bloco.objects.get(id=bloco_id).delete()
        except Bloco.DoesNotExist:
            raise NotFound(detail='Bloco não existe')

    def find_by_id(self, bloco_id):
        try:
            return Bloco.objects.get(id=bloco_id)
        except Bloco.DoesNotExist:
            raise NotFound(detail='Bloco não encontrado')