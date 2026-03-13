#!/bin/bash

echo "Build started"
pip install -r requirements.txt

echo "Collect static files"
python manage.py collectstatic --no-input
