import pytest
import io

from api_tests.utils.generate_image_file import generate_image_file

VALID_TYPE_SCENARIOS = [('JPEG', 200), ('PNG', 200)]
INVALID_TYPE_SCENARIOS = [(b"not an image", "NOT AN IMAGE"), (io.BytesIO(b""), "EMPTY FILE"),
                          (None, "NO FILE PROVIDED")]


@pytest.mark.API
@pytest.mark.IMAGE_UPLOAD_PET
@pytest.mark.PET
class TestImageUploadPet:
    
    @pytest.mark.parametrize("image_type, status_code", VALID_TYPE_SCENARIOS, ids=[x for x, _ in VALID_TYPE_SCENARIOS])
    def test_image_upload_pet(self, fxt_pet_api, fxt_add_pet, image_type, status_code):
        pet = fxt_add_pet
        
        file_name, bio = generate_image_file(image_type)
        files = {"file": ("corrupt.jpg", bio, "image/jpeg")}
        
        response = fxt_pet_api.upload_pet_image(pet_id=pet["id"], files=files)
        response.status_code == status_code
    
    @pytest.mark.parametrize("invalid_image, description", INVALID_TYPE_SCENARIOS,
                             ids=[x for _, x in INVALID_TYPE_SCENARIOS])
    def test_upload_invalid_pet_image(self, fxt_pet_api, fxt_add_pet, invalid_image, description):
        pet_id = fxt_add_pet["id"]
        
        if isinstance(invalid_image, io.BytesIO):
            invalid_image.seek(0)
            files = {"file": ("empty.png", invalid_image, "image/png")}
        elif isinstance(invalid_image, bytes):
            files = {"file": ("corrupt.jpg", io.BytesIO(invalid_image), "image/jpeg")}
        else:
            files = {}
        
        response = fxt_pet_api.upload_pet_image(pet_id, files=files, expected_failure=True)
        
        assert response.status_code in (400, 415), f"{description} should fail, got {response.status_code}"
