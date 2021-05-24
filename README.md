# django-api-project
Django rest api project

# For setting up local dev enviroment and running locally. 
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

# For running with docker container.
```sh
docker build -t <docker-repo-username>/scratch-api-demo:2.0 .
docker run -itd --name scratchapi -p 8000:8000 -v <host-path>:/app/src/data/db <image-name>(<docker-repo-username>/scratch-api-demo:2.0)
# Test by browsing URL http://<local-ip/localhost>:8000/v1/users/

```

# For running with kubernetes.
```sh
kubectl apply -f k8s-deployment.yaml
# App is running with `NodePort` service
# Test by browsing URL http://<local-ip/localhost>:30007/v1/users/

```