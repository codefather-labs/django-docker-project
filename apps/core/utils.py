from drf_yasg import openapi

from apps.core.api.models import base_api_response


def generate_api_response(
        success: bool,
        status: str = None,
        details_schema: openapi.Schema = None) -> base_api_response:
    return openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(
                type=openapi.TYPE_BOOLEAN, default=False if success else True
            ),
            'status': openapi.Schema(
                type=openapi.TYPE_STRING,
                default='Success' if success and not status else status if status else 'Failed',
            ),
            'details': details_schema if details_schema \
                else openapi.Schema(type=openapi.TYPE_OBJECT)
        })


def create_context(page_name: str, data=None):
    result = {
        "page_name": page_name
    }
    if data:
        result['context'].update(**data)

    return result


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
