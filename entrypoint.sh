#!/bin/bash

echo "Make migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate --run-syncdb

echo "Collect static files"
python manage.py collectstatic

# echo "Run service"
# uvicorn service1.asgi:application --host 0.0.0.0 --port 8000 --reload --lifespan off
