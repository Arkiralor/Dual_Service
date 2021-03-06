from os import sep
from SampleProject.settings import BASE_DIR

TOKEN_CSV_PATH = f"{BASE_DIR}{sep}notes{sep}tokens.csv"

class GoAPITasks:
    PRIMES = "prime_list"
    FACTORS = "find_factors"
    PRIME_FACTORS = "prime_factors"
    INT_TO_BINARY = "int_to_binary"
    BINARY_TO_INT = "binary_to_int"
    RANDOM_BINARY = "random_binary"
    FIBONACCI = "fibonacci"
    REG_ARITH_SERIES = "reg_arith_series"
    REG_GEO_SERIES = "reg_geo_series"
    PROJECTILE_PATH_2D = "projectile_path_2d"