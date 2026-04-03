#!/bin/bash

export RUPYSO_MODE=debug
export RUPYSO_DATABASE=mysql

/var/www/rupyso/.venv/bin/gunicorn \
    --access-logfile - \
    --workers 3 \
    --bind 127.0.0.1:8000 \
    Rupyso.wsgi:application