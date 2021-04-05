#!/bin/bash

if [ "$(id --user)" = "0" ]; then
    echo "Running the fix-perms script."
    fix-perms -r -u app_user -g app_group /app

    echo "Waiting for postgres ..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started."

    echo "Runing migrations..."
    python manage.py migrate

    echo "Running: gosu app_user "$@""
    exec gosu app_user "$@"
fi

exec "$@"