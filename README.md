# Dockerizing-a-Django-and-MySQL-Application
How to Connect your MySQL Database to your Dockerized Django Application.  making it easier to develop and deploy. In this tutorial, we will walk you through the process of dockerizing a Django and MySQL application.



### Step 1: Create a Dockerfile

In your Django project’s root directory, create a Dockerfile. This file defines how your Django application should be built inside a Docker container. Here's a basic Dockerfile for a Django application:


```dockerfile
FROM python:3.10.2
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN apt-get update
RUN pip install -r /requirements.txt
RUN mkdir /app
COPY . /app
WORKDIR /app

```


### Step 2: Create a docker-compose.yaml File

Next, create a docker-compose.yaml file in your project's root directory. This file defines the services and their configurations, including the Django application and MySQL database. Here's a basic docker-compose.yaml

```yml

version: '3.9'

services:

  django:
    image: dev_image
    container_name: dev
    build: .
    restart: always
    ports:
      - 8000:8000
    volumes:
      - .:/app
    command: sh -c "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"
    env_file:
      - .env
    depends_on:
      - db
    
  db:
    image: mysql
    container_name: mysql_db
    restart: always
    ports:
      - 3307:3306
    volumes:
      - data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${DATABASE_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DATABASE_NAME}
      MYSQL_USER: ${DATABASE_USER}
      MYSQL_PASSWORD: ${DATABASE_PASSWORD}

volumes:
  data:
```


### Step 3: Set Environment Variables

Create a .env file in your project's root directory to store environment variables for your Django application and MySQL database. Here's an example .env file

```env

DATABASE_NAME=db_name
DATABASE_USER=username
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=3306
DATABASE_ROOT_PASSWORD=root-password

```

### Step 4: Configure Django Settings 

In your Django project’s settings.py, make sure you read environment variables for sensitive information like SECRET_KEY and database settings. For example:

```python

DATABASES = dict(default={
    'ENGINE': 'django.db.backends.mysql',
    'NAME': str(os.getenv('DATABASE_NAME')),
    'USER': str(os.getenv('DATABASE_USER')),
    'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
    'PORT': str(os.getenv('DATABASE_PORT')),
    'PORT': '3306',
    'OPTIONS': {
        'charset': 'utf8mb4',
    }
})

```