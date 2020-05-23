from concurrent import futures
from logging import getLogger

import grpc
from grpc_reflection.v1alpha import reflection

from src.env import Env
from src.services import stanza_service, health_service
from src.proto import stanza_pb2_grpc, health_pb2_grpc, stanza_pb2, health_pb2

logger = getLogger(__name__)


def init_server(worker_threads: int) -> grpc.Server:
    pool = futures.ThreadPoolExecutor(max_workers=worker_threads)
    return grpc.server(pool)


def init_route(server: grpc.Server) -> None:
    stanza_pb2_grpc.add_StanzaServicer_to_server(stanza_service.StanzaService, server)
    health_pb2_grpc.add_HealthServicer_to_server(health_service.HealthService, server)

def init_reflection(server: grpc.Server) -> None:
    SERVICE_NAMES = (
        stanza_pb2.DESCRIPTOR.services_by_name['Stanza'].full_name,
        health_pb2.DESCRIPTOR.services_by_name['Health'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
