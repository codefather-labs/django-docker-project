from abc import abstractmethod, ABC
from enum import Enum
from typing import Optional

from datamodels import DataModel


class RequestMethod(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'

    def __str__(self):
        return self.value


class Request(DataModel):
    url: str
    headers: dict
    body: Optional[str]
    data: Optional[dict]
    method: RequestMethod


class AbstractClient(ABC):

    @property
    @abstractmethod
    def base_url(self): ...

    @property
    @abstractmethod
    def api_key(self): ...

    @abstractmethod
    def request(self, request: Request):
        ...
