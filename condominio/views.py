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
        result = {'data': 'Condomínio inserido com sucesso'}

        return Response(result)
