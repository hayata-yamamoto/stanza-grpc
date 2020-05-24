import os
from abc import ABC, abstractstaticmethod
from dataclasses import dataclass
from typing import Any, Dict

import environs


class AbstractEnv(ABC):
    @abstractstaticmethod
    def to_dict() -> Dict[str, Any]:
        pass

    @abstractstaticmethod
    def is_production() -> bool:
        pass


@dataclass(frozen=True, eq=True)
class Env(AbstractEnv):
    env = environs.Env()
    env.read_env()

    MODE: str = env.str('MODE', 'development')
    PORT: int = env.int('PORT', 50051)
    HOST: str = env.str("HOST", "127.0.0.1")
    NUM_THREADS: int = env.int("NUM_THREADS", 10)

    LANGUAGE: str = env.str("LANGUAGE", 'en')

    @staticmethod
    def to_dict() -> Dict[str, Any]:
        return Env.env.dump()

    @staticmethod
    def is_production() -> bool:
        return Env.MODE == 'production'
