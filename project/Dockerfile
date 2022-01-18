FROM python:3.8

WORKDIR /usr/src

RUN apt update
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
# RUN apk update
# RUN apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./requirenments.txt .
RUN pip install -r requirenments.txt 
COPY . .

CMD cd cloud_project & python manage.py makemigrations & python manage.py migrate & python manage.py runserver 0.0.0.0:8000
