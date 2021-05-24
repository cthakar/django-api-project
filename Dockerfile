FROM python:3.9.0
WORKDIR /app
COPY . /app/
RUN pip install pipenv && pipenv install --system
ENTRYPOINT [ "/bin/sh", "/app/run-app.sh" ]
