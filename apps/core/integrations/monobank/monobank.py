import json
import os
from urllib.parse import urljoin

import requests
from django.urls import reverse

from apps.core.integrations.interface import AbstractClient, Request, RequestMethod
from settings.environment.settings import get_settings_module

settings = get_settings_module()


class MonobankClient(AbstractClient):
    def __init__(self):
        self.__api_key = os.environ.get('MONOBANK_API_KEY')
        self.__base_url = 'https://api.monobank.ua'
        self.__headers = {
            "X-Token": self.api_key
        }

    @property
    def api_key(self):
        return self.__api_key

    @property
    def headers(self):
        return self.__headers

    @property
    def base_url(self):
        return self.__base_url

    def request(self, request: Request) -> requests.Response:
        query = {}
        query.update({
            "method": str(request.method),
            "url": request.url,
            "headers": request.headers,
        })
        if request.method == RequestMethod.POST:
            query['data'] = request.body

        return requests.request(**query)

    def create_webhook_url(self):
        return urljoin(
            f"{settings.PROTOCOL}://{settings.HOST}", reverse(
                "core-urls:integrations-urls:monobank-webhook-url"
            )
        )

    def add_webhook(self) -> requests.Response:
        url = urljoin(self.base_url, '/personal/webhook')
        data = {
            "webHookUrl": self.create_webhook_url()
        }

        return self.request(Request(
            url=url,
            headers=self.headers,
            method=RequestMethod.POST,
            body=json.dumps(data)
        ))

    def get_personal_client_info(self) -> requests.Response:
        url = urljoin(self.base_url, '/personal/client-info')

        return self.request(Request(
            url=url,
            headers=self.headers,
            method=RequestMethod.GET
        ))
