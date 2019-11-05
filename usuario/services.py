from .models import Usuario


class UsuarioService:

    def find(self):
        return Usuario.objects.all()

    def insert(self, params):
        usuario = Usuario()
        usuario.nome = params['nome']
        usuario.sobrenome = params['sobrenome']
        usuario.apartamento = params['apartamento']
        usuario.cpf = params['cpf']
        usuario.email = params['email']
        usuario.telefone = params['telefone']
        usuario.data_inicio_moradia = params['data_inicio_moradia']
        usuario.data_fim_moradia = params['data_fim_moradia']
        usuario.status = params['status']

        usuario.save()

        return usuario
