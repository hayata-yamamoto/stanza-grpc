import socket
from abc import ABC, abstractmethod
from logging import getLogger

logger = getLogger(__name__)


class AbstractHealthUsecase(ABC):
    @staticmethod
    @abstractmethod
    def alive() -> bool:
        pass


class HealthUsecase(AbstractHealthUsecase):
    @staticmethod
    def alive() -> bool:
        return True
