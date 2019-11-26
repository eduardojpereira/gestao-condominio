from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from bloco.serializers import BlocoResponseSerializer, BlocoInputSerializer
from bloco.services import BlocoService


class BlocoView(GenericAPIView):
    serializer_class = BlocoInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = BlocoService()

    def get(self, request):
        data = self.service.find()
        serialized = BlocoResponseSerializer(data, many=True)
        return Response(serialized.data)

    def post(self, request):
        params = request.data.copy()
        self.service.insert(params)

        result = {'detail': 'Bloco Cadastrado!'}
        return Response(result)


class BlocoViewId(GenericAPIView):
    serializer_class = BlocoInputSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = BlocoService()

    def put(self, request, bloco_id):
        params = request.data.copy()
        params['id'] = bloco_id

        self.service.update(params)

        result = {'data': 'Bloco atualizado com sucesso!'}

        return Response(result)

    def delete(self, request, bloco_id):
        self.service.delete(bloco_id)

        result = {'data': 'Bloco deletado com Sucesso'}

        return Response(result)

    def get(self, request, bloco_id):
        data = self.service.find_by_id(bloco_id)

        serializer = BlocoResponseSerializer(data)

        return Response(serializer.data)

