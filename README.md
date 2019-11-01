# Gestão de Condominios

Instalação do python no windows:

https://python.org.br/instalacao-windows/

https://www.python.org/downloads/release/python-374/

https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe


Rode os comandos abaixo no console/terminal:
```
$ sudo apt install python3-pip

$ sudo pip install pipenv
```

Após baixar o projeto, acesse a pasta do mesmo e execute os comandos abaixo:
```
$ pipenv install

$ pipenv shell
```

Instalar requerimentos:

```
pip install -r requeriments.txt
```


Crie um usuário e senha para logar no Django Admin:
```
python manage.py createsuperuser
```

Rode esse comando para subir o servidor:
```
python manage.py runserver
```

Acesse no navegador a url: http://localhost:8000

Depois tente acessar e logar no Django Admin com o usuário e senha criado acima: http://localhost:8000/admin/

A documentação do projeto se encontra em: http://localhost:8000/docs

### Orientação

Cada app deve seguir o seguinte formato:

![Captura de tela de 2019-10-27 22-56-44](https://user-images.githubusercontent.com/5925134/67646698-1fce8f80-f90e-11e9-9fd9-4b02f30a712a.png)

Para criar um app como o do exemplo acima, basta execupar o seguinte comando (Troque a palavra 'apartamento' pelo nome do seu app):

```
$ django-admin startapp apartamento
```

