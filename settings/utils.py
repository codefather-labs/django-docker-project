import os
import re

from django.urls import re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Codefather.dev API",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="GPL3"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,)
)


def custom_static_serve(prefix, view=serve, **kwargs):
    return [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs
        ),
    ]


def load_env(env_file_name: str):
    file = open(env_file_name, 'r', encoding='utf-8')
    data = file.read()
    file.close()

    strings = data.split("\n")
    for string in strings:
        if not string or string == '' or string.startswith("#"):
            continue

        os.environ.setdefault(string.split("=")[0], string.split("=")[1])
