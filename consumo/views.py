from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from consumo.serializers import ConsumoResponseSerializer
from consumo.services import ConsumoService


class ConsumoView(GenericAPIView):

    def __init__(self):
        super().__init__()
        self.service = ConsumoService()

    def get(self, request):
        data = self.service.find()
        serialized = ConsumoResponseSerializer(data, many=True)
        return Response(serialized.data)
