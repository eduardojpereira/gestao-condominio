from rest_framework.exceptions import NotFound
from consumo.models import Consumo


class ConsumoService:

    def find(self):
        return Consumo.objects.all()

    def insert(self, params):
        consumo = Consumo()
        consumo.apartamento_id = params['apartamento']
        consumo.leitor_id = params['leitor']
        consumo.leitura_atual = params['leitura_atual']
        consumo.data_leitura_atual = params['data_leitura_atual']
        consumo.save()

    def update(self, params):
        consumo_id = params['id']
        apartamento_id = params['apartamento']
        leitor_id = params['leitor']
        leitura_atual = params['leitura_atual']
        data_leitura_atual = params['data_leitura_atual']
        consumo = Consumo(id=consumo_id, apartamento_id=apartamento_id, leitor_id=leitor_id, leitura_atual=leitura_atual,
                          data_leitura_atual=data_leitura_atual)
        consumo.save(update_fields=['apartamento', 'leitor', 'leitura_atual', 'data_leitura_atual'])

    def delete(self, consumo_id):
        try:
            Consumo.objects.get(id=consumo_id).delete()
        except Consumo.DoesNotExist:
            raise NotFound(detail='Consumo não encontrado')

    def find_by_id(self, consumo_id):
        try:
            return Consumo.objects.get(id=consumo_id)
        except Consumo.DoesNotExist:
            raise NotFound(detail='Consumo não encontado')
