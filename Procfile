web: gunicorn simple_shop.wsgi --log-file -
web: python manage.py migrate && gunicorn simple_shop.wsgi