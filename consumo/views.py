from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from consumo.serializers import ConsumoInputSerializer
from consumo.serializers import ConsumoResponseSerializer
from consumo.services import ConsumoService


class ConsumoView(GenericAPIView):

    serializer_class = ConsumoInputSerializer

    def __init__(self):
        super().__init__()
        self.service = ConsumoService()

    def get(self, request):
        data = self.service.find()
        serialized = ConsumoResponseSerializer(data, many=True)
        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'data': 'Consumo registrado!'}
        return Response(result)

class ConsumoViewId(GenericAPIView):

    serializer_class = ConsumoInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ConsumoService()

    def put(self, request, consumo_id):
        params = request.data.copy()
        params['id'] = consumo_id
        self.service.update()
        result = {'data': 'Medição corrigida com sucesso'}
        return Response(result)

    def delete(self, request, consumo_id):
        self.service.delete(consumo_id)
        result = {'data': 'Medição deletada com sucesso'}
        return Response(result)

    def get(self, request, consumo_id):
        data = self.service.find_by_id(consumo_id)
        serializer = ConsumoResponseSerializer(data)
        return Response(serializer.data)
