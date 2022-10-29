from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def get(self, item): ...

    @abstractmethod
    def set(self, item, value): ...

    @abstractmethod
    def data(self): ...
