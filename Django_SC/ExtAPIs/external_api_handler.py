import requests

from globalconstants.masked_constants import GO_BASE_URL, PRIME_LIST_URL, \
    FIND_FACTORS_URL, PRIME_FACTORS_URL, INT_TO_BINARY_URL, BINARY_TO_INT_URL, RANDOM_BINARY_URL,\
    FIBONACCI_URL, REG_ARITH_SERIES_URL, REG_GEO_SERIES_URL, PROJECTILE_PATH_2D_URL
from globalconstants.global_constants import GoAPITasks


class GoAPIHandler:
    base_url = GO_BASE_URL
    prime_list_url = PRIME_LIST_URL
    find_factors_url = FIND_FACTORS_URL
    prime_factors_url = PRIME_FACTORS_URL
    int_to_binary_url = INT_TO_BINARY_URL
    binary_to_int_url = BINARY_TO_INT_URL
    random_binary_url = RANDOM_BINARY_URL
    fibonacci_url = FIBONACCI_URL
    reg_arith_series_url = REG_ARITH_SERIES_URL
    reg_geo_series_url = REG_GEO_SERIES_URL
    projectile_path_2d_url = PROJECTILE_PATH_2D_URL
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
        elif task is GoAPITasks.PRIME_FACTORS:
            resp = cls.find_prime_factors(query)
        elif task is GoAPITasks.INT_TO_BINARY:
            resp = cls.int_to_binary(query)
        elif task is GoAPITasks.BINARY_TO_INT:
            resp = cls.binary_to_int(query)
        elif task is GoAPITasks.RANDOM_BINARY:
            resp = cls.random_binary(query)
        elif task is GoAPITasks.FIBONACCI:
            resp = cls.fibonacci(query)
        elif task is GoAPITasks.REG_ARITH_SERIES:
            resp = cls.reg_arith_series(query)
        elif task is GoAPITasks.REG_GEO_SERIES:
            resp = cls.reg_geo_series(query)
        elif task is GoAPITasks.PROJECTILE_PATH_2D:
            resp = cls.projectile_path_2d(query)
        else:
            raise Exception(f"Error Go API response: Improper task name: {task}")
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
            raise Exception(f"Error Go API response: {resp.status_code} {resp.content}")

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
    def find_prime_factors(cls, query):
        params = {
            "num": query
        }
        return cls.make_request(
            url=cls.base_url+cls.prime_factors_url,
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

    @classmethod
    def fibonacci(cls, query):
        params = {
            'terms': query
        }
        return cls.make_request(
            url=cls.base_url+cls.fibonacci_url,
            params=params
        )

    @classmethod
    def reg_arith_series(cls, query):
        return cls.make_request(
            url=cls.base_url+cls.reg_arith_series_url,
            params = query
        )

    @classmethod
    def reg_geo_series(cls, query):
        return cls.make_request(
            url=cls.base_url+cls.reg_geo_series_url,
            params = query
        )

    @classmethod
    def projectile_path_2d(cls, query):
        return cls.make_request(
            url=cls.base_url+cls.projectile_path_2d_url,
            params = query
        )