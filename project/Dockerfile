FROM python:3.8

WORKDIR /usr/src

RUN apt update

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirenments.txt 

CMD cd cloud_project & python manage.py makemigrations & python manage.py migrate & python manage.py runserver 0.0.0.0:8000

# FROM python:3.8

# WORKDIR /usr/src

# RUN apt update

# RUN pip install --upgrade pip
# COPY requirenments.txt .
# RUN pip install -r requirenments.txt 
# COPY cloud_project/ .

# CMD python manage.py makemigrations & python manage.py migrate & python manage.py runserver 0.0.0.0:8000
