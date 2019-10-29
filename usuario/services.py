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

        usuario.save()

        return usuario
