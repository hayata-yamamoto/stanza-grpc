import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict

import environs


class AbstractEnv(ABC):
    @abstractmethod
    def to_dict() -> Dict[str, Any]:
        pass

    @abstractmethod
    def is_production() -> bool:
        pass


@dataclass(frozen=True, eq=True)
class Env:
    env = environs.Env()
    env.read_env()

    MODE: str = env.str('MODE', 'development')
    PORT: int = env.int('PORT', 50051)
    HOST: str = env.str("HOST", "127.0.0.1")
    NUM_THREADS: int = env.int("NUM_THREADS", 10)

    LANGUAGE: str = env.str("LANGUAGE", 'en')

    def to_dict(self) -> Dict[str, Any]:
        return env.dump()

    def is_production(self) -> bool:
        return self.MODE == 'production'
