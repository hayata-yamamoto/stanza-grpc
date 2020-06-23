import pytest
import os
from src.env import Env


def test_is_production(): 
    os.environ['MODE'] = 'development'
    assert Env().is_production == False

    os.environ["MODE"] = 'production'
    assert Env().is_production == True

