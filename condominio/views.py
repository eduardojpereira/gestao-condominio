from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import CondominioResponseSerializer
from .services import CondominioService


class CondominioView(GenericAPIView):

    def __init__(self):
        super().__init__()
        self.service = CondominioService()

    def get(self, request):
        data = self.service.find()
        serialized = CondominioResponseSerializer(data, many=True)

        return Response(serialized.data)
