FROM python:3.10.7

RUN mkdir /src
RUN mkdir /static

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY . /src/
WORKDIR /src

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate --run-syncdb && python manage.py migrate && python manage.py collectstatic && python manage.py test -v 2

CMD uvicorn service1.asgi:application --host 0.0.0.0 --port 8000 --reload --lifespan off

#CMD uvicorn service1.asgi:application --reload
#CMD gunicorn service1.wsgi:application -b 0.0.0.0:8000 --reload --workers=2
#CMD gunicorn service1.asgi:application -b 0.0.0.0:8000 --reload --workers=2 -k uvicorn.workers.UvicornWorker # most efficient in theory
