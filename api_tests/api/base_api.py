from abc import ABC
import requests


class BaseApi(ABC):
    
    def __init__(self, base_url: str = "https://petstore.swagger.io/v2"):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
    
    def _request(self, method: str, url: str, params=None, json=None, data=None, expected_failure=False,
                 custom_error_message=None, headers=None, files=None):
        full_url = f"{self.base_url}{url}"
        
        response = requests.request(
            method=method,
            url=full_url,
            params=params,
            json=json,
            data=data,
            headers=headers or self.headers,
            files=files
        )
        
        if not response.ok and not expected_failure:
            error_message = f"Request failed with status code {response.status_code}\nError: {response.text}"
            if custom_error_message:
                error_message += f"\n{custom_error_message}"
            raise Exception(error_message)
        if response.ok and expected_failure:
            raise Exception(f"Expected failure not raised\nResponse: {response.text}")
        
        return response
    
    def get(self, url: str, params=None, **kwargs):
        return self._request("GET", url, params=params, **kwargs)
    
    def post(self, url: str, json=None, data=None, **kwargs):
        return self._request("POST", url, json=json, data=data, **kwargs)
    
    def put(self, url: str, json=None, **kwargs):
        return self._request("PUT", url, json=json, **kwargs)
    
    def delete(self, url: str, **kwargs):
        return self._request("DELETE", url, **kwargs)
