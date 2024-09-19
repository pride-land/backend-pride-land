# Pride-Land &middot; [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![Static Badge](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

## Introduction 
Prideland a non-profit organization with a mission to create a society in which everyone, regardless of whether they are able-bodied or disabled, can work freely as they are by respecting their different physical, intellectual, and mental conditions and by giving appropriate consideration to each other.

## Overview
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

* Utilized by developers for rapid development
* The Web browsable API is a huge usability win for your developers.
* [Authentication policies][authentication] including optional packages for [OAuth1a][oauth1-section] and [OAuth2][oauth2-section].
* [Serialization][serializers] that supports both [ORM][modelserializer-section] and [non-ORM][serializer-section] data sources.
* Customizable all the way down - just use [regular function-based views][functionview-section] if you don't need the [more][generic-views] [powerful][viewsets] [features][routers].
* [Extensive documentation][docs].
## Requirements

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

## Example 

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

    pip install django
    pip install djangorestframework
    django-admin startproject example .
    ./manage.py migrate
    ./manage.py createsuperuser


Now edit the `example/urls.py` module in your project:

```python
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.ExampleModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff'] or fields = '__all__'


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL configuration.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Link your API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

We'd also like to configure a couple of settings for our API.

Add the following to your `settings.py` module:

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
```

We're almost done, now run the this

    python manage.py runserver

### Utilized Postgresql as database.

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

### for .env file settings:

```shell
DB_USER = "DB_USER"
DB_PASS = "DB_PASS"
DATABASE_URL = "DB_URL"
ALLOWED_HOSTS = ['*']
SECRET_KEY = "SECRET_KEY"
```

[oauth1-section]: https://www.django-rest-framework.org/api-guide/authentication/#django-rest-framework-oauth
[oauth2-section]: https://www.django-rest-framework.org/api-guide/authentication/#django-oauth-toolkit
[serializer-section]: https://www.django-rest-framework.org/api-guide/serializers/#serializers
[modelserializer-section]: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
[functionview-section]: https://www.django-rest-framework.org/api-guide/views/#function-based-views
[generic-views]: https://www.django-rest-framework.org/api-guide/generic-views/
[viewsets]: https://www.django-rest-framework.org/api-guide/viewsets/
[routers]: https://www.django-rest-framework.org/api-guide/routers/
[serializers]: https://www.django-rest-framework.org/api-guide/serializers/
[authentication]: https://www.django-rest-framework.org/api-guide/authentication/
[image]: https://www.django-rest-framework.org/img/quickstart.png
[docs]: https://www.django-rest-framework.org/
