from abc import ABC, abstractmethod
from logging import getLogger
from typing import Any, Dict, List

import stanza

logger = getLogger(__name__)


class AbstractStanzaUsecase(ABC):
    @abstractmethod
    def __init__(self, pipeline: stanza.Pipeline) -> None:
        pass

    @abstractmethod
    def recognize(self, sentence: str) -> List[Dict[str, Any]]:
        pass


class StanzaUsecase(AbstractStanzaUsecase):
    def __init__(self, pipeline: stanza.Pipeline) -> None:
        self.pipeline = pipeline

    def _recognize(self, sentence: str) -> List[Dict[str, Any]]:
        return self.pipeline(sentence).to_dict()

    def recognize(self, sentence: str) -> List[Dict[str, Any]]:
        return self._recognize(sentence)
