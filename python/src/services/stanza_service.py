import json
from abc import ABC, abstractmethod
from logging import getLogger
from typing import Any

import stanza
import grpc

from src.proto import stanza_pb2, stanza_pb2_grpc
from src.usecases.stanza_usecase import StanzaUsecase

logger = getLogger(__name__)


class StanzaService(stanza_pb2_grpc.StanzaServicer):
    def __init__(self, language: str) -> None:
        self.usecase = StanzaUsecase(stanza.Pipeline(language))

    def recognize_sentence(
        self, request: stanza_pb2.RecognizeSentenceRequest,
        contenxt: grpc.ServicerContext
    ) -> stanza_pb2.RecognizeSentenceResponse:
        """This function throw string content to stanza pipeline via StanzaUsecase. 

        Args:
            request (stanza_pb2.RecognizeSentenceRequest): gPRC request 
            contenxt (grpc.ServicerContext): gRPC context

        Returns:
            stanza_pb2.RecognizeSentenceResponse: This response contains recognized result
        """
        res = self.usecase.recognize(request.sentence)
        return stanza_pb2.RecognizeSentenceResponse(
            sentence=request.sentence,
            recognized_result=json.dumps(res.to_dict()))

    def RecognizeSentence(
        self, request: stanza_pb2.RecognizeSentenceRequest,
        contenxt: grpc.ServicerContext
    ) -> stanza_pb2.RecognizeSentenceResponse:
        """This function is interface of recognize_sentence function

        Args:
            request (stanza_pb2.RecognizeSentenceRequest): 
            contenxt (grpc.ServicerContext): 

        Returns:
            stanza_pb2.RecognizeSentenceResponse: 
        """
        return self.recognize_sentence(request, contenxt)
