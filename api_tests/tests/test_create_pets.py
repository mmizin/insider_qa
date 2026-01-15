from collections import namedtuple

import pytest

from api_tests.utils.api_payloads import create_pet_payload

CreatePetScenarios = namedtuple(
    "CreatePetScenarios",
    "scenario_id scenario_name id name category photoUrls tags status expected_failure status_code"
)

PET_SCENARIOS = [
    CreatePetScenarios(scenario_id=1, id=1, scenario_name="CREATE_VALID_PET", name="Meredith Palmer", category=None,
                       photoUrls=None, tags=None, status="available", expected_failure=False, status_code=200),
    CreatePetScenarios(scenario_id=2, scenario_name="CREATE_ONLY_WITH_ID_AND_NAME", id=2, name="Stanley Hudson",
                       category=None, photoUrls=None, tags=None, status="available", expected_failure=False,
                       status_code=200),
    CreatePetScenarios(scenario_id=3, scenario_name="INVALID_ID", id=9223372036854776000, name="Dwight Schrute",
                       category=None, photoUrls=None, tags=None, status="available", expected_failure=True,
                       status_code=500),
    CreatePetScenarios(scenario_id=4, scenario_name="DUPLICATED_ID", id=1, name="Michael Scot", category=None,
                       photoUrls=None, tags=None, status="available", expected_failure=True, status_code=500),
    CreatePetScenarios(scenario_id=5, scenario_name="INVALID_NAME", id=3, name=123, category=None, photoUrls=None,
                       tags=None, status="available", expected_failure=True, status_code=405),
    CreatePetScenarios(scenario_id=6, scenario_name="MISSED_ID", id=None, name="Andy Bernard", category=None,
                       photoUrls=None, tags=None, status="available", expected_failure=True, status_code=405),
    CreatePetScenarios(scenario_id=7, scenario_name="MISSED_NAME", id=4, name=None, category=None, photoUrls=None,
                       tags=None, status="available", expected_failure=True, status_code=405)
]


@pytest.mark.API
@pytest.mark.CREATE_PET
@pytest.mark.PET
class TestCreatePets:
    
    @pytest.mark.parametrize("scenario", PET_SCENARIOS, ids=lambda x: f"scenario #{x.scenario_id} | {x.scenario_name}")
    def test_create_pet(self, fxt_pet_api, scenario):
        payload = create_pet_payload(id=scenario.id, name=scenario.name)
        if scenario.scenario_name == "MISSED_ID":
            del payload["id"]
        elif scenario.scenario_name == "CREATE_ONLY_WITH_ID_AND_NAME":
            del payload["category"]
            del payload["tags"]
            del payload["status"]
        
        response = fxt_pet_api.create_pet(json=payload, expected_failure=scenario.expected_failure)
        
        if scenario.expected_failure:
            assert response.status_code == scenario.status_code
        else:
            response = response.json()
            assert response["id"] == scenario.id
            fxt_pet_api.delete_pet(pet_id=scenario.id)
