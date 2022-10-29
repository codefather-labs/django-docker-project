from typing import Union

from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication

from apps.core.api import models, constants
from apps.core.utils import generate_api_response
from settings.logger import system_message


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening
