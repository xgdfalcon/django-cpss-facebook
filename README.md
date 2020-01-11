> ## 🛠 Status: In Development
> django-cpss-facebook currently in development.

# Python Facebook API - Django  [<img src="https://github.com/xgdfalcon/django-cpss-facebook/blob/master/facebook-django/static/cpss/logo.png?raw=true" alt="CPSS by XGDFalcon®" height="20px" />](https://controlpointsw.com) 

[![Build Status](https://travis-ci.org/xgdfalcon/django-cpss-facebook.svg?branch=master)](https://travis-ci.org/xgdfalcon/django-cpss-facebook)
[![PyPI version](https://badge.fury.io/py/django-cpss-facebook.svg)](https://badge.fury.io/py/django-cpss-facebook)

## Description

This is the [Django](https://www.djangoproject.com/) component that helps to integrate aspects of facebook into your application

## Django version

This project will focus on the currently supported Django releases as
stated on the [Django Project Supported Versions table](https://www.djangoproject.com/download/#supported-versions).

Backward compatibility with unsupported versions won't be enforced.

## Documentation

Project documentation is available at TBP.

## Setup

1. Add "django-cpss-facebook" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = [
        ...
        'facebook-django.CPSSFacebookConfig',
    ]
```
2. Run `python manage.py migrate` to create the django-cpss-facebook models.


## Contributing
See the [CONTRIBUTING.md](CONTRIBUTING.md) document for details.

## Versioning
This project follows [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html).

## License
This project follows the Apache license. See the [LICENSE](LICENSE) for details.

