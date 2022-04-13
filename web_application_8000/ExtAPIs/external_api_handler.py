import http
import requests

from globalconstants.masked_constants import GO_BASE_URL, PRIME_LIST_URL, \
    FIND_FACTORS_URL, INT_TO_BINARY_URL, RANDOM_BINARY_URL

class GoAPIHandler:
    base_url = GO_BASE_URL
    prime_list_url = PRIME_LIST_URL
    find_factors_url = FIND_FACTORS_URL
    int_to_binary_url = INT_TO_BINARY_URL
    random_binary_url = RANDOM_BINARY_URL
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
        }

    @classmethod
    def make_request(cls, task:str="", param = 0):
        if task == "prime_list":
            params = {
                "upper_limit": param
            }

            resp = requests.get(
                cls.base_url+cls.prime_list_url, 
                params=params,
                headers=cls.headers
            )

            if resp.status_code == 200:
                return resp.json()
            else:
                raise Exception(
                    status_code=404, 
                    detail="Item not found"
                )
        elif task == "find_factors":
            params = {
                "num": param
            }

            resp = requests.get(
                cls.base_url+cls.find_factors_url, 
                params=params,
                headers=cls.headers
            )

            if resp.status_code == 200:
                return resp.json()
            else:
                raise Exception(
                    status_code=404, 
                    detail="Item not found"
                )
        elif task == "int_to_binary":
            params = {
                "num": param
            }

            resp = requests.get(
                cls.base_url+cls.int_to_binary_url, 
                params=params,
                headers=cls.headers
            )

            if resp.status_code == 200:
                return resp.json()
            else:
                raise Exception(
                    status_code=404, 
                    detail="Item not found"
                )

        elif task == "random_binary":
            params = {
                "bits": param
            }

            resp = requests.get(
                cls.base_url+cls.random_binary_url, 
                params=params,
                headers=cls.headers
            )

            if resp.status_code == 200:
                return resp.json()
            else:
                raise Exception(
                    status_code=404, 
                    detail="Item not found"
                )
            
        