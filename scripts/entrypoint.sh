#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python -m skycruise.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

exec poetry run gunicorn skycruise.project.wsgi:application -w 4 -b 0.0.0.0:8000
