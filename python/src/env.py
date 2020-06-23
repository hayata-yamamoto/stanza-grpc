import os
from dataclasses import dataclass
from typing import Any, Dict
import environs


@dataclass(frozen=True, eq=True)
class Env:
    env = environs.Env()
    env.read_env()

    MODE: str = env.str('MODE', 'development')
    PORT: int = env.int('PORT', 50051)
    HOST: str = env.str("HOST", "127.0.0.1")
    NUM_THREADS: int = env.int("NUM_THREADS", 10)

    LANGUAGE: str = env.str("LANGUAGE", 'en')

    @staticmethod
    def is_production() -> bool:
        return Env.MODE == 'production'

    @staticmethod
    def address() -> str: 
        return f"{Env.HOST}:{Env.PORT}"