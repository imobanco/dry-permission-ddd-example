COMPOSER := docker-compose
DEV:=--file docker-compose.yml


################################################################################
# Dev container commands
################################################################################
build:
	$(COMPOSER) $(DEV) build $(args)

up:
	$(COMPOSER) $(DEV) up -d $(args)

down:
	$(COMPOSER) $(DEV) down $(args)

logs:
	$(COMPOSER) $(DEV) logs -f $(args)

up.psql:
	$(COMPOSER) $(DEV) up -d postgres

up.logs: up logs

config:
	$(COMPOSER) $(DEV) config

bash:
	$(COMPOSER) $(DEV) run django bash

bash.psql:
	$(COMPOSER) $(DEV) run postgres bash

bash.celery:
	$(COMPOSER) $(DEV) run celery bash

test:
	$(COMPOSER) $(DEV) run django python manage.py test --parallel $(shell nproc) $(args)

shell:
	$(COMPOSER) $(DEV) run django python manage.py shell

makemigrations:
	$(COMPOSER) $(DEV) run django python manage.py makemigrations $(args)

migrate:
	$(COMPOSER) $(DEV) run django python manage.py migrate $(args)

restart:
	$(COMPOSER) $(DEV) restart

restart.django:
	$(COMPOSER) $(DEV) restart django

stop:
	$(COMPOSER) $(DEV) stop

stop.django:
	$(COMPOSER) $(DEV) stop django

remove.volumes:
	$(COMPOSER) $(DEV) down -v

coverage:
	$(COMPOSER) $(DEV) run django coverage run --source='.' manage.py test --parallel $(shell nproc) $(args)
	$(COMPOSER) $(DEV) run django coverage report
	$(COMPOSER) $(DEV) run django coverage html
	$(COMPOSER) $(DEV) run django coverage xml

populate.superuser:
	-$(COMPOSER) $(DEV) run django python manage.py loaddata initial_superuser.json

################################################################################
# Bare host commands
################################################################################
pip.install:
	pip install --upgrade -r requirements-dev.txt

fmt:
	black .

fmt.check:
	black --check .
	flake8

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop

config.env:
	cp .env.example .env
