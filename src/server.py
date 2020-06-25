from concurrent import futures
from logging import getLogger

import grpc
from grpc_reflection.v1alpha import reflection

from src.env import Env
from src.services import stanza_service, health_service
from src.pb2 import stanza_pb2_grpc, health_pb2_grpc, stanza_pb2, health_pb2

logger = getLogger(__name__)
__version__ = "0.1.0"


def _init_route(server: grpc.Server) -> None:
    stanza_pb2_grpc.add_StanzaServicer_to_server(
        stanza_service.StanzaService(Env.LANGUAGE), server)
    health_pb2_grpc.add_HealthServicer_to_server(
        health_service.HealthService(), server)


def _init_reflection(server: grpc.Server) -> None:
    SERVICE_NAMES = (
        stanza_pb2.DESCRIPTOR.services_by_name['Stanza'].full_name,
        health_pb2.DESCRIPTOR.services_by_name['Health'].full_name,
        reflection.SERVICE_NAME)
    reflection.enable_server_reflection(SERVICE_NAMES, server)


def init_server() -> grpc.Server:
    pool = futures.ThreadPoolExecutor(max_workers=Env.NUM_THREADS)
    server = grpc.server(pool)

    _init_route(server)
    _init_reflection(server)

    server.add_insecure_port(Env.address())
    return server
