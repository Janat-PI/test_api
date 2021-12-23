run:
	python manage.py runserver

migrates:
	python manage.py makemigrations
	python manage.py migrate

venv:
	python3 -m venv venv && source ./venv/bin/activate
	pip install -r requirements.txt
