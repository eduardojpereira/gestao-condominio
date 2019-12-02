from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserInputSerializer
from .serializers import UserResponseSerializer
from .services import UserManager


class UserView(GenericAPIView):

    serializer_class = UserInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserManager()

    def get(self, request):
        data = self.service.find()
        serialized = UserResponseSerializer(data, many=True)

        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)
        result = {'data': 'Usuário inserido com sucesso'}

        return Response(result)
