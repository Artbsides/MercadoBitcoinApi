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

redis:  ## Up redis in background mode
	@docker-compose up -d redis

postgres:  ## Up postgres in background mode
	@docker-compose up -d postgres

packages:  ## Run pip install packages
	@COMPOSE_DEVELOPMENT_COMMAND="pip install -r requirements/tests.txt" \
		docker-compose -f compose.yml -f compose.development.yml up app

database-migrations:  ## Run alembic database migrations
	@COMPOSE_DEVELOPMENT_COMMAND="alembic upgrade head" \
		docker-compose -f compose.yml -f compose.development.yml up app

tests: -B  ## Run api tests
	@COMPOSE_DEVELOPMENT_COMMAND="python -m pytest -s" \
		docker-compose -f compose.yml -f compose.development.yml up app

code-convention:  ## Run code convention
	@COMPOSE_DEVELOPMENT_COMMAND="flake8 Api ApiTests" \
		docker-compose -f compose.yml -f compose.development.yml up app

secrets:  ## Encrypt or decrypt secrets. environment=staging|production action=encrypt|decrypt
ifeq ("$(action)", "encrypt")
	@SECRETS_PATH=".k8s/$(environment)/secrets"
	@SECRETS_PUBLIC_KEY="$$(cat $$SECRETS_PATH/.sops.yml | awk "/age:/" | sed "s/.*: *//" | xargs -d "\r")"

	@sops -e -i --encrypted-regex "^(data|stringData)$$" -a $$SECRETS_PUBLIC_KEY \
		$$SECRETS_PATH/.secrets.yml

	@echo "==== Ok"

else ifeq ("$(action)", "decrypt")
	@SECRETS_KEY="$$(kubectl get secret sops-age --namespace argocd -o yaml | awk "/sops-age.txt:/" | sed "s/.*: *//" | base64 -d)"

	@SOPS_AGE_KEY=$$SECRETS_KEY sops -d -i .k8s/$(environment)/secrets/.secrets.yml && \
		echo "==== Ok"

else
	@echo "==== Action not found."
endif

github-tag:  ## Create or delete github tags. action=create|delete tag=[0-9].[0-9].[0-9]-staging|[0-9].[0-9].[0-9]
ifeq ("$(action)", "create")
	@git tag $(tag) && \
		git push origin $(tag)

else ifeq ("$(action)", "delete")
	@git tag -d $(tag) && \
		git push origin :refs/tags/$(tag)

else
	@echo "==== Action not found."
endif

run:  ## Run api. mode=development|latest
ifeq ("$(mode)", "latest")
	@docker-compose up app
else ifeq ("$(mode)", "development")
	@COMPOSE_DEVELOPMENT_COMMAND="python -u -m debugpy --listen ${APP_HOST}:${APP_DEBUG_PORT} -m uvicorn Main:app --host ${APP_HOST} --port ${APP_HOST_PORT} --reload" \
		docker-compose -f compose.yml -f compose.development.yml up app
else
	@echo ==== Mode not found.
endif


%:
	@:
