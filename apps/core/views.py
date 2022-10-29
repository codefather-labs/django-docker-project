from django.core.handlers.asgi import ASGIRequest

from django.shortcuts import render
from django.views.decorators.cache import cache_page

from apps.core.utils import get_client_ip, create_context
from settings.environment.settings import environment, Environment, get_settings_module

settings = get_settings_module()


def cache_production_only(func):
    if environment == Environment.PRODUCTION:
        @cache_page(60 * 15)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
    else:
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

    return wrapper


@cache_production_only
def main(request: ASGIRequest):
    return render(
        request,
        'site/main.html',
        create_context('main')
    )


@cache_production_only
def handler400(request: ASGIRequest):
    return render(
        request,
        'site/400.html',
        create_context('thanks'), status=400
    )


@cache_production_only
def handler404(request: ASGIRequest):
    return render(
        request,
        'site/404.html',
        create_context('thanks'), status=404
    )


@cache_production_only
def handler500(request: ASGIRequest):
    return render(
        request,
        'site/500.html',
        create_context('thanks'), status=500
    )
