from django.urls import path
from ExtAPIs.views import FindPrimesInRangeView, FindFactors, PrimeFactorView, RandomBinaryNumber, BinaryToInt, IntToBinary, \
    FibonacciView, RegArithSeriesView, RegGeoSeriesView

urlpatterns = [
    path('primesinrange/', FindPrimesInRangeView.as_view(), name="find_primes_in_range"),
    path('factors/', FindFactors.as_view(), name="find_factors"),
    path('prime_factors/', PrimeFactorView.as_view(), name="find_prime_factors"),
    path('randombinary/', RandomBinaryNumber.as_view(), name="random_binary_number"),
    path('binarytoint/', BinaryToInt.as_view(), name="binary_to_int"),
    path('inttobinary/', IntToBinary.as_view(), name="int_to_binary"),
    path('fibonacci/', FibonacciView.as_view(), name="fibonacci_sequence"),
    path('arith_series/', RegArithSeriesView.as_view(), name="arithmetic_series"),
    path('geo_series/', RegGeoSeriesView.as_view(), name="geometric_series"),
]
