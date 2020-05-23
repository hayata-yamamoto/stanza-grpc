import pytest

from src.usecases.health_usecase import HealthUsecase


def test_alive():
    assert True == HealthUsecase.alive()
