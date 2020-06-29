from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.middleware.csrf import get_token


def language(request: WSGIRequest) -> dict:
    return {'LANGUAGE_CODE': settings.LANGUAGE_CODE}


def csrf_token(request: WSGIRequest) -> dict:
    return {'csrf_token': get_token(request)}
