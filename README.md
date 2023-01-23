# How to set-up a Django project

### Install and Activate virtual environment

``` bash
python -m venv .venv

(windows)- .venv/Scripts/activate
```

### Install project dependencies
``` bash
    pip install -r requirements/local.txt

    pip install -r requirements/production.txt
```

### How to run make and run migrations

``` bash
   local (windows) 
   py manage.py migrate --settings=config.settings.local

   py manage.py makemigrations --settings=config.settings.local


   production (windows) 
      py manage.py migrate --settings=config.settings.production

       py manage.py makemigrations --settings=config.settings.production

```

### How to run the project
---
``` bash
   local (windows) - py manage.py runserver --settings=config.settings.local

   production (windows) - py manage.py runserver --settings=config.settings.production

```

