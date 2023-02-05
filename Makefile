.PHONY: default
default: runserver

runserver:
	python manage.py runserver

create_superuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations sync_files

init_migrations:
	rm -dfr sync_files/migrations/
	@make migrations

migrate:
	python manage.py migrate

sync:
	python manage.py sync