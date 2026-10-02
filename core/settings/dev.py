from .base import *
from decouple import config,Csv

SECRET_KEY=config('SECRET_KEY',default='test')
DEBUG=config('DEBUG',cast=bool,default='True')
ALLOWED_HOSTS=config('ALLOWED_HOSTS',cast=Csv())