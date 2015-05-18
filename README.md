# People Service

Data representation for civil servants, initially powering profiles.

# Init

Once the stack is up, in a new terminal initialise the database with:

    docker-compose run --rm people python manage.py db init
    docker-compose run --rm people python manage.py db migrate
    docker-compose run --rm people python manage.py db upgrade
