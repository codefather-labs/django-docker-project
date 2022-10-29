from drf_yasg import openapi

from settings.environment.settings import get_settings_module

settings = get_settings_module()

base_api_response = openapi.Schema(
    type=openapi.TYPE_OBJECT, properties={
        "error": openapi.Schema(type=openapi.TYPE_BOOLEAN),
        "status": openapi.Schema(type=openapi.TYPE_STRING),
        "details": openapi.Schema(type=openapi.TYPE_OBJECT),
    }
)
