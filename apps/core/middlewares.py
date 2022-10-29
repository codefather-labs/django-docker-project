from django.core.handlers.asgi import ASGIRequest
from django.middleware.http import MiddlewareMixin

from settings.environment.settings import get_settings_module

settings = get_settings_module()


class CustomMiddleware(MiddlewareMixin):
    def process_response(self, request: ASGIRequest, response):
        ...
        return response
