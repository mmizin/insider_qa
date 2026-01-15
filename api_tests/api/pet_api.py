from io import BytesIO
from typing import Optional

from api_tests.api.base_api import BaseApi
from api_tests.utils.enums import PetStatus


class PetApi(BaseApi):
    
    def __init__(self):
        super().__init__()
    
    def create_pet(self, json: dict, expected_failure=False, headers=None):
        url = "/pet"
        error_message = f"Failed to add pet"
        
        response = self.post(url=url, json=json, expected_failure=expected_failure, custom_error_message=error_message,
                             headers=headers)
        return response
    
    def delete_pet(self, pet_id: int, expected_failure=False):
        url = f"/pet/{pet_id}"
        error_message = f"Failed to delete pet with id {pet_id}"
        
        response = self.delete(url=url, expected_failure=expected_failure, custom_error_message=error_message)
        return response
    
    def get_pet(self, pet_id: int, expected_failure=False, params: Optional[dict] = None):
        url = f"/pet/{pet_id}"
        error_message = f"Failed to get pet with id {pet_id}"
        
        response = self.get(url=url, params=params, expected_failure=expected_failure,
                            custom_error_message=error_message)
        return response
    
    def get_pet_by_status(self, status: PetStatus, expected_failure=False, params: Optional[dict] = None):
        status = status if not isinstance(status, PetStatus) else status.value
        url = f"/pet/findByStatus?status={status}"
        error_message = f"Failed to find pet by status {status}"
        
        response = self.get(url=url, params=params, expected_failure=expected_failure,
                            custom_error_message=error_message)
        return response
    
    def update_pet_form(self, pet_id: int, data: dict, expected_failure=False):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        url = f"/pet/{pet_id}"
        
        response = self.post(url=url, data=data, expected_failure=expected_failure, headers=headers)
        return response
    
    def update_pet(self, json, expected_failure=False):
        url = "/pet"
        error_message = "Failed to update pet"
        
        response = self.put(url=url, json=json, expected_failure=expected_failure, custom_error_message=error_message)
        return response
    
    def upload_pet_image(self, pet_id: int, files: dict[tuple], expected_failure=False):
        headers = {"accept": "application/json"}
        url = f"/pet/{pet_id}/uploadImage"
        error_message = f"Failed to upload pet image for pet with id {pet_id}"
        
        response =  self.post(url=url, files=files, expected_failure=expected_failure, headers=headers, eric_error_message=error_message)
        return response
