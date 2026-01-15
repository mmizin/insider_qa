import random
import pytest

from collections import namedtuple
from api_tests.utils.api_payloads import create_pet_payload
from api_tests.utils.enums import PetStatus

GetPetScenarios = namedtuple(
    "GetPetScenarios",
    "scenario_id scenario_name expected_failure status_code"
)

PET_SCENARIOS = [
    GetPetScenarios(scenario_id=1, scenario_name="GET_VALID_PET", expected_failure=False, status_code=200),
    GetPetScenarios(scenario_id=2, scenario_name="GET_NON_EXISTING_PET", expected_failure=True, status_code=404),
]


@pytest.mark.API
@pytest.mark.GET_PET
@pytest.mark.PET
class TestGetPets:
    
    @pytest.mark.parametrize("scenario", PET_SCENARIOS, ids=lambda x: f"scenario #{x.scenario_id} | {x.scenario_name}")
    def test_get_pet(self, fxt_pet_api, fxt_add_pet, scenario):
        pet = fxt_add_pet
        params = {"pet_id": pet["id"]}

        if scenario.scenario_name == "GET_NON_EXISTING_PET":
            params["pet_id"] += random.randint(10, 100)

        response = fxt_pet_api.get_pet(**params, expected_failure=scenario.expected_failure)
        assert response.status_code == scenario.status_code
    
    @pytest.mark.parametrize("_fxt_add_pet", [status for status in PetStatus] + ["*invalid_status*"], indirect=['_fxt_add_pet'])
    def test_get_pet_by_status(self, fxt_pet_api, _fxt_add_pet):
        pet, status = _fxt_add_pet
        params = {"expected_failure": True if status == "*invalid_status*" else False}
        
        response = fxt_pet_api.get_pet_by_status(status=status, **params)
        pets = response.json()
        if status not in ["*invalid_status*"]:
            assert pet in pets, f"Pet with id {pet['id']} was not found in the list of pets with status {status}"
        else:
            assert response.status_code == 400
        

@pytest.fixture
def _fxt_add_pet(request, fxt_pet_api):
    status = request.param
    if status in ["*invalid_status*"]:
        pet = None
    else:
        id = random.randint(1, 1000)
        name = f"Pet {id}"
        payload = create_pet_payload(id=id, name=name, status=status.value)
        response = fxt_pet_api.create_pet(json=payload)
        pet = response.json()
    yield pet, status
    if status not in  ["*invalid_status*"]:
        fxt_pet_api.delete_pet(pet_id=pet["id"])
