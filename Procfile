# web: newrelic-admin run-program gunicorn linbees.wsgi -b "0.0.0.0:$PORT" -w 3
web: newrelic-admin run-program waitress-serve --port=$PORT linbees.wsgi:application