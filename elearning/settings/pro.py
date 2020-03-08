from .base import *


DEBUG = False

ADMINS = (
    ('Amin A', 'amin@example.com'),
)


ALLOWED_HOSTS = ['elearningproject.com', 'www.elearningproject.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elearning',
        'USER': 'elearning',
        'PASSWORD': 'testpassword',
    }
}
