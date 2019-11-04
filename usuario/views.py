from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UsuarioInputSerializer
from .serializers import UsuarioResponseSerializer
from .services import UsuarioService


class UsuarioView(GenericAPIView):

    serializer_class = UsuarioInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UsuarioService()

    def get(self, request):
        data = self.service.find()
        serialized = UsuarioResponseSerializer(data, many=True)

        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'data': 'Usuário inserido com sucesso'}

        return Response(result)
