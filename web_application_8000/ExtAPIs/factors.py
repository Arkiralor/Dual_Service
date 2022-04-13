from typing import List

class Factor:
    lower_limit = 2


    @classmethod
    def get_factors(cls, num:int)->List[int]:
        factors = [1, num]
        upper_limit = num//2
        for i in range(cls.lower_limit, upper_limit + 1):
            if num % i == 0:
                factors.append(i)
        return list(sorted(set(factors)))