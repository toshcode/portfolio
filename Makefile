SHELL := /bin/bash

include .env

install:
	pipenv install

shell:
	python manage.py shell

serve:
	python manage.py runserver

drymigration:
	python manage.py makemigrations --dry-run --verbosity 3

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

herokumigrate:
	heroku run python manage.py migrate

superuser:
	python manage.py createsuperuser

test:
	python manage.py test