.PHONY: install
install:
	poetry install --no-root

.PHONY: migrations
migrations:
	 poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	 poetry run python manage.py migrate

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: update
update: install migrate install-pre-commit ;

.PHONY: shell
shell:
	 poetry run python manage.py shell

.PHONY: dbshell
dbshell:
	 poetry run python manage.py dbshell

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: test-stepwise
test-stepwise:
	poetry run pytest --reuse-db --sw -vv --show-capture=no

.PHONY: lint-and-test
lint-and-test: lint test ;
