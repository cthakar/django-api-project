# django-api-project
Django rest api project


```sh
python manage.py migrate
### Optional Steps started
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=<email-of-your-choice>
export DJANGO_SUPERUSER_PASSWORD=<password-of-your-choice>
python manage.py createsuperuser --noinput
### Optinal steps finished
python manage.py load_test_data
export DJANGO_DEBUG=False # Change it if you want to run with True
python manage.py runserver 0.0.0.0:8000
```