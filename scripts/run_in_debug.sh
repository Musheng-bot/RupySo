#!/bin/bash

export RUPYSO_MODE=debug
export RUPYSO_DATABASE=sqlite3

SCRIPT_PATH=$(readlink -f $0)
WORKSPACE=$(dirname $(dirname $SCRIPT_PATH))

$WORKSPACE/.venv/bin/python $WORKSPACE/manage.py runserver