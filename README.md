[![Build Status](https://travis-ci.org/livingbio/django-template.svg?branch=master)](https://travis-ci.org/livingbio/django-template)

# Weather Parser

## INSTALLATION & SETTINGS

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

Then edit the SECRET_KEY in local.env file, replace `{{ secret_key }}` into any [Django Secret Key](http://www.miniwebtool.com/django-secret-key-generator/), for example:

   SECRET_KEY=twvg)o_=u&@6^*cbi9nfswwh=(&hd$bhxh9iq&h-kn-pff0&&3

Run migrations:

    python manage.py migrate

### Documentation

You can use [mkdocs](http://www.mkdocs.org/) to write beatuiful documentations. By typing:

    mkdocs serve

Then you can see your document in http://localhost:8001/

### Detailed instructions

Take a look at the docs for more information.

