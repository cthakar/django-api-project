cd /app/src/
if [ -e data/db/db.sqlite3 ]
then
    echo "Running with existing db"
    python manage.py collectstatic --noinput
    python manage.py runserver 0.0.0.0:8000
else
    echo "Running without existing db"
    python manage.py migrate
    python manage.py load_test_data
    python manage.py collectstatic --noinput
    python manage.py runserver 0.0.0.0:8000 
fi
