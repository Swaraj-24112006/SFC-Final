"""
Test settings for running unit tests with SQLite in-memory DB
without requiring an external running PostgreSQL instance.
"""
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'OPTIONS': {
            'timeout': 30,
        },
    }
}
