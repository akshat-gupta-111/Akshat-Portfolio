#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting gunicorn on port ${PORT:-3000}..."
exec gunicorn api.wsgi:application \
    --bind "0.0.0.0:${PORT:-3000}" \
    --workers 2 \
    --timeout 120
