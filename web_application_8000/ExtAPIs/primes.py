from typing import List

class PrimeNumber:
    lower_limit = 2

    @classmethod
    def find_primes_in_range(cls, upper_limit:int) -> List[int]:
        list_of_primes = []
        for num in range(cls.lower_limit, upper_limit + 1):
            if cls.is_prime(num):
                list_of_primes.append(num)
        return list_of_primes

    @classmethod
    def is_prime(cls, num:int)->bool:
        flag = True
        if num < 2:
            flag = False
        for i in range(2, num):
            if num % i == 0:
                flag = False
        return flag