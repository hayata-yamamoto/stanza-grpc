import socket
from abc import ABC, abstractstaticmethod
from logging import getLogger
from src.proto import health_pb2, health_pb2_grpc

logger = getLogger(__name__)


class AbstractHealthUsecase(ABC):
    @abstractstaticmethod
    def alive() -> bool:
        pass


class HealthUsecase(AbstractHealthUsecase):
    @staticmethod
    def alive() -> bool:
        return True
