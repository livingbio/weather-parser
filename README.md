[![Build Status](https://travis-ci.org/livingbio/django-template.svg?branch=master)](https://travis-ci.org/livingbio/django-template)

# Django Template for GliaCloud

This is a django template for gliacloud

## INSTALLATION & SETTINGS

### Install Django

To install django, type the following command

    sudo pip install django

### Create Django project from the template

To create the project, run the following command and please replace your_project_name to what you like :

    django-admin.py startproject --template=https://github.com/livingbio/django-template/archive/master.zip --extension=py,md,yml,ini your_project_name

### Setting Virtualenv

At first, you should make sure you have [virtualenv](http://www.virtualenv.org/) installed.

after that, just cd to your_project_name:

    cd your_project_name

Then create your virtualenv:

    virtualenv venv

Second, you need to enable the virtualenv by

    source venv/bin/activate

Install all dependencies:

    pip install -r requirements.txt

Settings are stored in environment variables via [django-environ](http://django-environ.readthedocs.org/en/latest/). The quickiest way to start is to rename `local.sample.env`

    cp weather/src/weather/settings/local.sample.env weather/src/weather/settings/local.env

Run migrations:

    python manage.py migrate

### Documentation

You can use [mkdocs](http://www.mkdocs.org/) to write beatuiful documentations. By typing:

    mkdocs serve

Then you can see your document in http://localhost:8001/

### Detailed instructions

Take a look at the docs for more information.

