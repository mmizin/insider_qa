import random
import pytest

from collections import namedtuple
from api_tests.utils.api_payloads import create_pet_payload

DeletePetScenarios = namedtuple(
    "GetPetScenarios",
    "scenario_id scenario_name expected_failure status_code"
)

PET_SCENARIOS = [
    DeletePetScenarios(scenario_id=1, scenario_name="DELETE_VALID_PET", expected_failure=False, status_code=200),
    DeletePetScenarios(scenario_id=2, scenario_name="DELETE_NON_EXISTING_PET", expected_failure=True, status_code=404),
]


@pytest.mark.API
@pytest.mark.DELETE_PET
@pytest.mark.PET
class TestDeletePets:
    
    @pytest.mark.parametrize("scenario", PET_SCENARIOS, ids=lambda x: f"scenario #{x.scenario_id} | {x.scenario_name}")
    def test_delete_pet(self, fxt_pet_api, _fxt_add_pet, scenario):
        pet = _fxt_add_pet
        params = {"pet_id": pet["id"]}
        
        if scenario.scenario_name == "DELETE_NON_EXISTING_PET":
            params["pet_id"] += random.randint(10, 100)
        
        response = fxt_pet_api.delete_pet(expected_failure=scenario.expected_failure, **params)
        assert response.status_code == scenario.status_code


@pytest.fixture
def _fxt_add_pet(fxt_pet_api):
    id = random.randint(1, 1000)
    name = f"Pet {id}"
    payload = create_pet_payload(id=id, name=name)
    
    response = fxt_pet_api.create_pet(json=payload)
    return response.json()
