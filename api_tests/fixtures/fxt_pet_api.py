import pytest
from api_tests.api.pet_api import PetApi


@pytest.fixture
def fxt_pet_api():
    """Returns an instance of PetApi"""
    return PetApi()
