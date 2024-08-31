# Project-Pride-Land

## introduction

## Installing / Getting started

Our Back-End Tech stack: <br>

```
• Python
• Django Rest
``` 
### Setting up Development

Here's a quick guide and run down on how to setup environment and start developing the project.
Make sure to add a .env file that has DB_USER and DB_PASS

#### Initial Setup:

```
$ git clone: https://github.com/pride-land/backend-pride-land
$ cd backend-pride-land
```

#### Quick start:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install django
$ python3 manage.py runserver
```

#### App or Dependencies installed:

```
$ pip install djangorestframework
$ pip install django-cors-headers
$ pip install psycopg2-binary
$ pip install python-dotenv
$ pip install djangorestframework-simplejwt
$ pip install Pillow
```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prideland',
        'USER': 'postgres',
        'PASSWORD': 'your_password', 
        'HOST': 'your_localhost',
        'PORT': 'your_localport',
    }

