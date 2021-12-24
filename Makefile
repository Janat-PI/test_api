run:
	python manage.py runserver

migrates:
	python manage.py makemigrations
	python manage.py migrate

venv:
	python3 -m venv venv && source ./venv/bin/activate
	pip install -r requirements.txt

gun:
	gunicorn core.wsgi --reload

network:
	python manage.py runserver 10.117.15.147:8000
