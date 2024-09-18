# Pride-Land &middot; [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![Static Badge](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

## introduction 
Prideland a Non-profit Organization with a mission to create a society in which everyone, regardless of whether they are able-bodied or disabled, can work freely as they are by respecting their different physical, intellectual, and mental conditions and by giving appropriate consideration to each other.

## Overview
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

* Utilized by developers for rapid development
* The Web browsable API is a huge usability win for your developers.
* [Authentication policies][authentication] including optional packages for [OAuth1a][oauth1-section] and [OAuth2][oauth2-section].
* [Serialization][serializers] that supports both [ORM][modelserializer-section] and [non-ORM][serializer-section] data sources.
* Customizable all the way down - just use [regular function-based views][functionview-section] if you don't need the [more][generic-views] [powerful][viewsets] [features][routers].
* [Extensive documentation][docs], and [great community support][group].

##
# Requirements

* Python 3.8+
* Django 5.0, 5.1+


## Installing / Getting started

Install: <br>

```shell
• Python
• Django Rest
``` 
### Setting up Development

Here's a quick guide and run down on how to setup environment and start developing the project.
Make sure to add a .env file that has DB_USER and DB_PASS

#### Initial Setup:

```shell
$ git clone: https://github.com/pride-land/backend-pride-land
$ cd backend-pride-land
```

#### Quick start:

```shell
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

Utilized Postgresql as database.

```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prideland',
        'USER': 'postgres',
        'PASSWORD': 'your_password', 
        'HOST': 'your_localhost',
        'PORT': 'your_localport',
    }
```

for .env file settings:

```shell
DB_USER = "DB_USER"
DB_PASS = "DB_PASS"
DATABASE_URL = "DB_URL"
ALLOWED_HOSTS = ['*']
SECRET_KEY = "SECRET_KEY"
```