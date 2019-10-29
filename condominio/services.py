from rest_framework.exceptions import NotFound

from .models import Condominio


class CondominioService:

    def find(self):
        return Condominio.objects.all()

    def insert(self, params):
        condominio = Condominio()
        condominio.cnpj = params['cnpj']
        condominio.endereco = params['endereco']
        condominio.nome = params['nome']

        condominio.save()

    def update(self, params):
        condominio_id = params['id']
        cnpj = params['cnpj']
        endereco = params['endereco']
        nome = params['nome']

        condominio = Condominio(id=condominio_id, cnpj=cnpj, endereco=endereco, nome=nome)
        condominio.save(update_fields=['cnpj', 'endereco', 'nome'])

    def delete(self, condominio_id):
        try:
            Condominio.objects.get(id=condominio_id).delete()
        except Condominio.DoesNotExist:
            raise NotFound(detail='Condomínio não encontrado')

    def find_by_id(self, condominio_id):
        try:
            return Condominio.objects.get(id=condominio_id)
        except Condominio.DoesNotExist:
            raise NotFound(detail='Condomínio não encontrado')
