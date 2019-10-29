from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import LeitorInputSerializer
from .serializers import LeitorResponseSerializer
from .services import LeitorService


class LeitorView(GenericAPIView):

    serializer_class = LeitorInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = LeitorService()

    def get(self, request):
        data = self.service.find()
        serialized = LeitorResponseSerializer(data, many=True)

        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'data': 'Leitor inserido com sucesso'}

        return Response(result)
