# Gestão de Condominios

Instalação do python no windows:

https://python.org.br/instalacao-windows/
https://www.python.org/downloads/release/python-374/
https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe


Rode os comandos abaixo no console/terminal:
```
sudo apt install python3-pip

sudo pip install pipenv

pipenv install

pipenv shell
```

Crie um usuário e senha para logar no Django Admin:
```
python manage.py createsuperuser --email seuemail@gmail.com --username seuusername
```

Rode esse comando para subir o servidor:
```
python manage.py runserver
```

Acesse no navegador a url: http://localhost:8000

Depois tente acessar e logar no Django Admin com o usuário e senha criado acima: http://localhost:8000/admin/