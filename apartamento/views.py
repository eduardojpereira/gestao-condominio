from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apartamento.serializers import ApartamentoResponseSerializer, ApartamentoInputSerializer
from apartamento.services import ApartamentoService


class ApartamentoView(GenericAPIView):

    serializer_class = ApartamentoInputSerializer

    def __init__(self):
        super().__init__()
        self.service = ApartamentoService()

    def get(self, request):
        data = self.service.find()
        serialized = ApartamentoResponseSerializer(data, many=True)

        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'detail': 'Apartamento inserido com sucesso'}

        return Response(result)

class ApartamentoViewId(GenericAPIView):

    serializer_class = ApartamentoInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ApartamentoService()

    def put(self, request, apartamento_id):
        params = request.data.copy()
        params['id'] = apartamento_id
        self.service.update(params)

        result = {'detail': 'Apartamento atualizado com sucesso'}

        return Response(result)

    def delete(self, request, apartamento_id):
        self.service.delete(apartamento_id)

        result = {'detail': 'Apartamento deletado com sucesso'}

        return Response(result)

    def get(self, request, apartamento_id):
        data = self.service.find_by_id(apartamento_id)

        serializer = ApartamentoResponseSerializer(data)

        return Response(serializer.data)
