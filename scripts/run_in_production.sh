#!/bin/bash

export RUPYSO_MODE=release
export RUPYSO_DATABASE=mysql

SCRIPT_PATH=$(readlink -f $0)
WORKSPACE=$(dirname $(dirname $SCRIPT_PATH))
source $WORKSPACE/.venv/bin/activate

$WORKSPACE/.venv/bin/gunicorn \
    --access-logfile - \
    --workers 3 \
    --bind 127.0.0.1:8000 \
    RupySo.wsgi:application
