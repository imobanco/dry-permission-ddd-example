FROM imobanco/python:dev-latest

WORKDIR /app

USER root

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY requirements*.txt /app/

RUN pip install --upgrade pip \
 && pip install -r requirements-dev.txt

USER app_user:app_group

COPY entrypoint.sh /usr/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
