import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()

if not env.bool('IGNORE_APPENV_FILE', default=False):
    ENV_FILE_PATH = os.path.join(BASE_DIR, '.env')
    if os.path.exists(ENV_FILE_PATH):
        env.read_env(ENV_FILE_PATH)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    'SECRET_KEY',
    default='9sylwbj#&s14)+5!p%4yzl^lx)rx_ato=*&x+spjat5k%=gmy3'
)

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS: list = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cleanup',

    'online_market',
    'online_market.products',
    'online_market.users',
    'online_market.orders',
    'online_market.carts',
]

# Settings for custom User model

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CART_SESSION_ID = 'cart'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'online_market.middleware.InitCartInSession',
    'online_market.middleware.Handle443Redirects',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ROOT_URLCONF = 'online_market.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'online_market.context_processors.language',
                'online_market.context_processors.csrf_token',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_market.wsgi.application'


# Database

DATABASES = {
    'default': env.db('DATABASE', '')
}

if not DATABASES['default']:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = env.str('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'online_market', 'static', 'css'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'online_market', 'media')
MEDIA_URL = '/media/'
