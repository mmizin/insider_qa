import random
import pytest

from collections import namedtuple
from api_tests.utils.api_payloads import create_pet_payload, update_pet_payload
from api_tests.utils.enums import PetStatus

UpdatePetScenarios = namedtuple(
    "ImageUploadPetScenarios",
    "scenario_id pet_id scenario_name data expected_failure status_code"
)

PET_FORM_SCENARIOS = [
    UpdatePetScenarios(scenario_id=1, pet_id=None, scenario_name="UPDATE_VALID_PET",
                       data={"name": "Jim Halpert", "status": random.choice(list(PetStatus))},
                       expected_failure=False, status_code=200),
    UpdatePetScenarios(scenario_id=2, pet_id=random.randint(100, 10000), scenario_name="UPDATE_NON_EXISTING_PET",
                       data={"name": "Jim Halpert", "status": random.choice(list(PetStatus))},
                       expected_failure=True, status_code=404),
    UpdatePetScenarios(scenario_id=3, pet_id=None, scenario_name="EMPTY_DATA",
                       data={}, expected_failure=True, status_code=405),
    UpdatePetScenarios(scenario_id=4, pet_id=None, scenario_name="INVALID_DATA_PROPERTIES",
                       data={"some": "text"}, expected_failure=True, status_code=405),
]

PET_SCENARIO = [
    UpdatePetScenarios(scenario_id=1, pet_id=None, scenario_name="UPDATE_VALID_PET", data=None, expected_failure=False,
                       status_code=200),
    UpdatePetScenarios(scenario_id=1, pet_id=9223372036854776000, scenario_name="UPDATE_WITH_INVALID_PET_ID", data=None,
                       expected_failure=True, status_code=500),
UpdatePetScenarios(scenario_id=2, pet_id=random.randint(100, 10000), scenario_name="UPDATE_NON_EXISTING_PET",
                       data={"name": "Jim Halpert", "status": random.choice(list(PetStatus))},
                       expected_failure=True, status_code=404),
]


@pytest.mark.API
@pytest.mark.UPDATE_PET
class TestUpdatePets:

    @pytest.mark.parametrize("scenario", PET_FORM_SCENARIOS,
                             ids=lambda x: f"scenario #{x.scenario_id} | {x.scenario_name}")
    def test_update_pet_form(self, fxt_pet_api, fxt_add_pet, scenario):
        pet = fxt_add_pet
        pet_id = scenario.pet_id or pet["id"]

        response = fxt_pet_api.update_pet_form(pet_id, data=scenario.data, expected_failure=scenario.expected_failure)
        assert response.status_code == scenario.status_code
    
    @pytest.mark.parametrize("scenario", PET_SCENARIO,
                             ids=lambda x: f"scenario #{x.scenario_id} | {x.scenario_name}")
    def test_update_pet(self, fxt_pet_api, _fxt_add_pet, scenario):
        pet = _fxt_add_pet
        pet_id = scenario.pet_id or pet["id"]
        new_id = pet_id + 1 if not scenario.pet_id else pet_id
        new_name = f"New_Pet {new_id}"
        new_status = random.choice(list(PetStatus))
        payload = update_pet_payload(id=new_id, name=new_name, status=new_status.value)
        
        try:
            response = fxt_pet_api.update_pet(json=payload, expected_failure=scenario.expected_failure)
            updated_pet = response.json()
            if not scenario.expected_failure:
                assert updated_pet["id"] == new_id
                assert updated_pet["name"] == new_name
                assert updated_pet["status"] == new_status.value
            else:
                assert response.status_code == scenario.status_code
        finally:
            try:
                fxt_pet_api.delete_pet(pet_id=pet["id"])
            except Exception:
                fxt_pet_api.delete_pet(pet_id=new_id)


@pytest.fixture
def _fxt_add_pet(fxt_pet_api):
    id = random.randint(1, 1000)
    name = f"Pet {id}"
    payload = create_pet_payload(id=id, name=name)
    response = fxt_pet_api.create_pet(json=payload)
    pet = response.json()
    
    return pet
