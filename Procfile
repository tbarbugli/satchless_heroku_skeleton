web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT py/settings.py
worker: bin/python py/manage.py celeryd -E -B --loglevel=INFO
