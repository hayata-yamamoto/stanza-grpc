from abc import ABC, abstractmethod
from logging import getLogger
from typing import Any, Dict, List
import json

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

    def _recognize(self, sentence: str) -> str:
        """Recognize sentences by stanza pipeline

        Args:
            sentence (str): Sentence user want to analyze

        Returns:
            List[Dict[str, Any]]: Analyzed information
        """
        data = self.pipeline(sentence).to_dict()
        return json.dumps(data)

    def recognize(self, sentence: str) -> str:
        return self._recognize(sentence)
