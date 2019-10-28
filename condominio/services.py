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

        return condominio
