import json
from abc import ABC, abstractmethod
from logging import getLogger
from typing import Any, Iterator

import grpc
from src.proto import health_pb2, health_pb2_grpc
from src.usecases.health_usecase import HealthUsecase

logger = getLogger(__name__)


class HealthService(health_pb2_grpc.HealthServicer):
    def Check(self, request: health_pb2.HealthCheckRequest,
              context: grpc.ServicerContext) -> health_pb2.HealthCheckResponse:
        return HealthUsecase.alive()

    def Watch(self, request) -> Iterator[bool]:
        yield HealthUsecase.alive()
