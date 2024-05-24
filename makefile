.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	 poetry run python -m skycruise.manage makemigrations

.PHONY: migrate
migrate:
	 poetry run python -m skycruise.manage migrate

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: update
update: install migrate install-pre-commit ;

.PHONY: shell
shell:
	 poetry run python -m skycruise.manage shell

.PHONY: dbshell
dbshell:
	 poetry run python -m skycruise.manage dbshell

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: run-server
run-server:
	poetry run python -m skycruise.manage runserver 192.168.1.8:8000

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: superuser
superuser:
	poetry run python -m skycruise.manage createsuperuser

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: test-stepwise
test-stepwise:
	poetry run pytest --reuse-db --sw -vv --show-capture=no

.PHONY: lint-and-test
lint-and-test: lint test ;
