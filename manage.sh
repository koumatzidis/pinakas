#!/bin/sh

export DJANGO_SETTINGS_MODULE=pinakas.settings.local

exec poetry run python3 manage.py "$@"
