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

    def recognize_sentence(self, sentence: str) -> str:
        """This function throw string content to stanza pipeline via StanzaUsecase. 

        Args:
            request (stanza_pb2.RecognizeSentenceRequest): gPRC request 
            contenxt (grpc.ServicerContext): gRPC context

        Returns:
            stanza_pb2.RecognizeSentenceResponse: This response contains recognized result
        """
        res = self.usecase.recognize(sentence)
        return res
    
    def RecognizeSentence(self, request, context):
        """This function is interface of recognize_sentence function

        Args:
            request (stanza_pb2.RecognizeSentenceRequest): 
            contenxt (grpc.ServicerContext): 

        Returns:
            stanza_pb2.RecognizeSentenceResponse: 
        """
        logger.debug("RecognizedSentence was passed")
        res = self.recognize_sentence(request.sentence)
        return stanza_pb2.RecognizeSentenceResponse(
            recognized_result=res)
