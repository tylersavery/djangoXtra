# DjangoXtra

> An updated version of the DjangoX starter pack


## 🚀 Features

- Django 5.0 & Python 3.12
- Install via [Pip](https://pypi.org/project/pip/) or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v5](https://getbootstrap.com/)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- Custom 404, 500, and 403 error pages
- SCSS support
- Vite support for JS bundling
- Django Ninja for API
- dotenv for local environment management

----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Docker](#docker)
  * [Environment](#environment)


----

## 📖 Installation
DjangoXtra can be installed via Pip or Docker. To start, clone the repo to your local computer and change into the proper directory.


### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Docker Compose

Use docker compose to setup your database and redis instance

```
docker compose --app my-project-name up --build --detach
```


### Environment
Copy the `example.env` file and update to your liking. Many other env vars exist. Browse the settings module for more.
```
cp example.env .env
```

