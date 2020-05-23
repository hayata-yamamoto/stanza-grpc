import socket
from abc import ABC, abstractmethod
from logging import getLogger
from src.proto import health_pb2, health_pb2_grpc

logger = getLogger(__name__)


class AbstractHealthUsecase(ABC):
    @staticmethod
    @abstractmethod
    def alive() -> bool:
        pass


class HealthUsecase(AbstractHealthUsecase):
    def alive() -> bool:
        return True
