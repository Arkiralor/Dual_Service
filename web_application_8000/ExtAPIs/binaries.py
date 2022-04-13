import random as rand
class Binary:

    @classmethod
    def random_binary_number(cls, length:int)->int:
        binary_number = 0
        while len(binary_number) < length:
            new_bit = rand.randint(0, 1)
            binary_number = binary_number * 10 + new_bit
        return binary_number

    @classmethod
    def int_to_binary(cls, num:int)->int:
        binary_number = ""
        while num > 0:
            binary_number = str(num % 2) + binary_number
            num = num // 2
        return int(binary_number)

    @classmethod
    def binary_to_int(cls, binary_number:int)->int:
        num = 0
        while binary_number > 0:
            num = num * 2 + binary_number % 10
            binary_number = binary_number // 10
        return num