from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from bloco.serializers import BlocoResponseSerializer
from bloco.services import BlocoService


class BlocoView(GenericAPIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = BlocoService()

    def get(self, request):
        data = self.service.find()
        serialized = BlocoResponseSerializer(data, many=True)
        return Response(serialized.data)



