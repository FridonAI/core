from abc import ABC, abstractmethod


class BaseUtility(ABC):
    @abstractmethod
    async def __call__(self, *args, **kwargs):
        pass
