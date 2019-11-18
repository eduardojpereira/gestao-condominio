from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import CondominioInputSerializer
from .serializers import CondominioResponseSerializer
from .services import CondominioService


class CondominioView(GenericAPIView):

    serializer_class = CondominioInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CondominioService()

    def get(self, request):
        data = self.service.find()
        serialized = CondominioResponseSerializer(data, many=True)

        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'detail': 'Condomínio inserido com sucesso'}

        return Response(result)

class CondominioViewId(GenericAPIView):

    serializer_class = CondominioInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CondominioService()

    def put(self, request, condominio_id):
        params = request.data.copy()
        params['id'] = condominio_id
        self.service.update(params)

        result = {'detail': 'Condomínio atualizado com sucesso'}

        return Response(result)

    def delete(self, request, condominio_id):
        self.service.delete(condominio_id)

        result = {'detail': 'Condomínio deletado com sucesso'}

        return Response(result)

    def get(self, request, condominio_id):
        data = self.service.find_by_id(condominio_id)

        serializer = CondominioResponseSerializer(data)

        return Response(serializer.data)
