from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apartamento.serializers import ApartamentoResponseSerializer
from apartamento.services import ApartamentoService


class ApartamentoView(GenericAPIView):

    def __init__(self):
        super().__init__()
        self.service = ApartamentoService()

    def get(self, request):
        data = self.service.find()
        serialized = ApartamentoResponseSerializer(data, many=True)

        return Response(serialized.data)
