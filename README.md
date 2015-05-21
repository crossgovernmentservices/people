# People Service

[![Build Status](https://travis-ci.org/crossgovernmentservices/people.svg)](https://travis-ci.org/crossgovernmentservices/people)

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Data representation for civil servants, initially powering profiles.

This service is smoke and mirrors and doesn't care about authentication nor authorisation (yet).

# Create a user

Provide an email address to the ```create_user``` management command:

    docker-compose run --rm people python manage.py create_user -e user@example.org

This just creates the DB schema for the user, and nothing else.

API calls can now just use this email address.

# Test

    # from dev-env directory
    docker-compose run --rm people python manage.py test
