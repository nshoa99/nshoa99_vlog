from distutils.command.config import config

from nsh_site.nsh_site.settings.dev import ALLOWED_HOSTS, DEBUG
from .base import *
import django_on_heroku
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'nsh-blog.herokuapp.com',
]