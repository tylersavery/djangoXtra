
install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

release:
	python manage.py migrate

web:
	gunicorn project.wsgi --log-file -

worker:
	celery --app=project worker --without-heartbeat --without-gossip --without-mingle --loglevel=INFO

build_styles:
	sass --quiet ./frontend/styles/main.scss ./static/css/main.css

watch_styles:
	sass --watch --quiet ./frontend/styles/main.scss ./static/css/main.css