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



redis:  ## A
	@docker-compose up -d redis

postgres:  ## A
	@docker-compose up -d postgres

packages:  ## A
	@COMPOSE_DEVELOPMENT_COMMAND="pip3 install -r requirements/development.txt" \
		docker-compose -f compose.yml -f compose.development.yml up mercado-bitcoin-api

database-migrations:  ## A
	@alembic upgrade head

run:  ## A
	@uvicorn Api.Main:app --reload


%:
	@:
