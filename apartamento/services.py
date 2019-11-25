from rest_framework.exceptions import NotFound

from apartamento.models import Apartamento


class ApartamentoService():

    def find(self):
        return Apartamento.objects.all()

    def insert(self, params):
        apartamento = Apartamento()
        apartamento.numero = params['numero']
        apartamento.esta_disponivel = params['esta_disponivel']
        apartamento.bloco_id = params['bloco']

        apartamento.save()

    def update(self, params):
        id = params['id']
        numero = params['numero']
        esta_disponivel = params['esta_disponivel']
        bloco_id = params['bloco']

        apartamento = Apartamento(id=id, numero=numero, esta_disponivel=esta_disponivel, bloco_id=bloco_id)
        apartamento.save(update_fields=['numero', 'esta_disponivel', 'bloco_id'])

    def delete(self, apartamento_id):
        try:
            Apartamento.objects.get(id=apartamento_id).delete()
        except Apartamento.DoesNotExist:
            raise NotFound(detail='Apartamento não encontrado')

    def find_by_id(self, apartamento_id):
        try:
            return Apartamento.objects.get(id=apartamento_id)
        except Apartamento.DoesNotExist:
            raise NotFound(detail='Apartamento não encontrado')
