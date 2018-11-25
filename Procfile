web: gunicorn config.wsgi:application
worker: celery worker --app=backend.taskapp --loglevel=info
