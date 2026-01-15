import random

import pytest

from api_tests.utils.api_payloads import create_pet_payload


@pytest.fixture
def fxt_add_pet(fxt_pet_api):
    id = random.randint(1, 1000)
    name = f"Pet {id}"
    payload = create_pet_payload(id=id, name=name)
    
    response = fxt_pet_api.create_pet(json=payload)
    pet = response.json()
    yield pet
    fxt_pet_api.delete_pet(pet_id=pet["id"])
 
