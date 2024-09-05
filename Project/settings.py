"""
Django settings for Project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

DATABASES = dict(default={
    'ENGINE': 'django.db.backends.mysql',
    'NAME': str(os.getenv('DATABASE_NAME')),
    'USER': str(os.getenv('DATABASE_USER')),
    'PASSWORD': str(os.getenv('DATABASE_PASSWORD')),
    'HOST': str(os.getenv('DATABASE_HOST')),
    'PORT': '3306',
    'OPTIONS': {
        'charset': 'utf8mb4',
    }
})
