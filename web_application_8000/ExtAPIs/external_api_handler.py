import http
import requests

from globalconstants.masked_constants import GO_BASE_URL, PRIME_LIST_URL, \
    FIND_FACTORS_URL, INT_TO_BINARY_URL, BINARY_TO_INT_URL, RANDOM_BINARY_URL
from globalconstants.global_constants import GoAPITasks


class GoAPIHandler:
    base_url = GO_BASE_URL
    prime_list_url = PRIME_LIST_URL
    find_factors_url = FIND_FACTORS_URL
    int_to_binary_url = INT_TO_BINARY_URL
    binary_to_int_url = BINARY_TO_INT_URL
    random_binary_url = RANDOM_BINARY_URL
    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }

    @classmethod
    def dispatch(cls, task: str = "", query=0):
        if task is GoAPITasks.PRIMES:
            resp = cls.find_prime_list(query)
        elif task is GoAPITasks.FACTORS:
            resp = cls.find_factors(query)
        elif task is GoAPITasks.INT_TO_BINARY:
            resp = cls.int_to_binary(query)
        elif task is GoAPITasks.BINARY_TO_INT:
            resp = cls.binary_to_int(query)
        elif task is GoAPITasks.RANDOM_BINARY:
            resp = cls.random_binary(query)
        else:
            raise Exception(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Invalid task"
            )
        return resp

    @classmethod
    def make_request(cls, url, params):
        resp = requests.get(
            url=url,
            params=params,
            headers=cls.headers
        )
        if resp.status_code in (200, 201, 202):
            return resp.json()
        else:
            raise Exception(
                status_code=resp.status_code,
                detail=resp.content
            )

    @classmethod
    def find_prime_list(cls, query):
        params = {
            "upper_limit": query
        }
        return cls.make_request(
            url=cls.base_url+cls.prime_list_url,
            params=params
        )

    @classmethod
    def find_factors(cls, query):
        params = {
            "num": query
        }
        return cls.make_request(
            url=cls.base_url+cls.find_factors_url,
            params=params
        )

    @classmethod
    def int_to_binary(cls, query):
        params = {
            "num": query
        }
        return cls.make_request(
            url=cls.base_url+cls.int_to_binary_url,
            params=params
        )

    @classmethod
    def random_binary(cls, query):
        params = {
            "bits": query
        }
        return cls.make_request(
            url=cls.base_url+cls.random_binary_url,
            params=params
        )

    @classmethod
    def binary_to_int(cls, query):
        params = {
            "binary_number": query
        }
        return cls.make_request(
            url=cls.base_url+cls.binary_to_int_url,
            params=params
        )
