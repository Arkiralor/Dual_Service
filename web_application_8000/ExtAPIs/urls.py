from django.urls import path
from ExtAPIs.views import FindPrimesInRangeView, FindFactors, PrimeFactorView, RandomBinaryNumber, BinaryToInt, IntToBinary

urlpatterns = [
    path('primesinrange/', FindPrimesInRangeView.as_view(), name="find_primes_in_range"),
    path('factors/', FindFactors.as_view(), name="find_factors"),
    path('prime_factors/', PrimeFactorView.as_view(), name="find_prime_factors"),
    path('randombinary/', RandomBinaryNumber.as_view(), name="random_binary_number"),
    path('binarytoint/', BinaryToInt.as_view(), name="binary_to_int"),
    path('inttobinary/', IntToBinary.as_view(), name="int_to_binary"),
]