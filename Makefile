pipenv-setup:
	pipenv install

pipenv-setup-dev:
	pipenv install --dev

run-server:
	python manage.py runserver

test:
	python manage.py test --settings=gestaocondominio.settings.testing

coverage:
	coverage run --source='.' manage.py test --settings=gestaocondominio.settings.testing
	coverage report

coverage-erase:
	coverage erase

code-convention:
	flake8
	pycodestyle

collect-static:
	python manage.py collectstatic

compile-messages:
	python manage.py compilemessages

make-migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate
