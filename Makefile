.ONESHELL:

SHELL  = /bin/bash
PYTHON = /usr/bin/python3

-include .env
export


define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("	%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@echo "Usage: make <command>"
	@echo "Options:"
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)



build:  ## Build images
	@docker-compose build

	@echo
	@docker-compose -f compose.yml -f compose.development.yml build

redis:  ## A
	@docker-compose up -d redis

postgres:  ## A
	@docker-compose up -d postgres

packages:  ## A
	@COMPOSE_DEVELOPMENT_COMMAND="pip install -r requirements/tests.txt" \
		docker-compose -f compose.yml -f compose.development.yml up app

database-migrations:  ## A
	@COMPOSE_DEVELOPMENT_COMMAND="alembic upgrade head" \
		docker-compose -f compose.yml -f compose.development.yml up appalembic upgrade head

tests: -B  ## Run api tests
	@COMPOSE_DEVELOPMENT_COMMAND="python -m pytest" \
		docker-compose -f compose.yml -f compose.development.yml up app

code-convention:  ## Run code convention
	@COMPOSE_DEVELOPMENT_COMMAND="flake8 Api ApiTests" \
		docker-compose -f compose.yml -f compose.development.yml up app

run:  ## Run api. mode=development|production
ifeq ("$(mode)", "production")
	@docker-compose up app
else ifeq ("$(mode)", "development")
	@COMPOSE_DEVELOPMENT_COMMAND="uvicorn Main:app --host ${APP_HOST} --port ${APP_HOST_PORT} --reload" \
		docker-compose -f compose.yml -f compose.development.yml up app
else
	@echo ==== Mode not found.
endif


%:
	@:
