# People Service

Data representation for civil servants, initially powering profiles.

This service is smoke and mirrors and doesn't care about authentication nor authorisation (yet).

# Init

Once the stack is up, in a new terminal initialise the database with:

    # from dev-env directory
    docker-compose run --rm people python manage.py db init
    docker-compose run --rm people python manage.py db migrate
    docker-compose run --rm people python manage.py db upgrade

# Test

    # from dev-env directory
    docker-compose run --rm people python manage.py test

