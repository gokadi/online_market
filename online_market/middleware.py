from typing import Callable

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponseBase
from django.shortcuts import redirect


class InitCartInSession:
    def __init__(
        self, get_response: Callable[[WSGIRequest], HttpResponseBase]
    ) -> None:
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> HttpResponseBase:
        if not request.session.get(settings.CART_SESSION_ID):
            request.session[settings.CART_SESSION_ID] = []

        return self.get_response(request)


class Handle443Redirects:
    def __init__(
        self, get_response: Callable[[WSGIRequest], HttpResponseBase]
    ) -> None:
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> HttpResponseBase:
        if settings.DEBUG:
            return self.get_response(request)

        request_uri = request.build_absolute_uri(
            request.get_full_path()
        )
        if '/users/' in request.path_info:
            if not request.is_secure():
                new_url = request_uri.replace('http:', 'https:')
                return redirect(new_url, permanent=False)
            return self.get_response(request)
        elif request.is_secure():
            new_url = request_uri.replace('https:', 'http:')
            return redirect(new_url, permanent=False)

        return self.get_response(request)
