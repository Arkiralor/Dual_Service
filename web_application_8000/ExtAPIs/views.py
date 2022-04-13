from datetime import datetime
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExtAPIs.primes import PrimeNumber
from ExtAPIs.factors import Factor
from ExtAPIs.binaries import Binary
from ExtAPIs.external_api_handler import GoAPIHandler

# Create your views here.

'''
Stand-Alone API Views.
'''

# class FindPrimesInRangeView(APIView):
#     '''
#     API to find all Prime numbers in a given range
#     '''
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         upper_limit = int(request.query_params.get('upper_limit', 0))
#         list_of_primes = PrimeNumber.find_primes_in_range(upper_limit)
#         resp = {
#             "primes": list_of_primes,
#             "lenght": len(list_of_primes),
#             "requesting_user": request.user.username
#         }

#         return Response(
#             resp,
#             status=status.HTTP_200_OK
#         )


# class FindFactors(APIView):
#     '''
#     API to find all factors of a given number
#     '''
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         number = int(request.query_params.get('number', 10))
#         factors = Factor.get_factors(number)
#         resp = {
#             "solution":{
#                 "number": number,
#                 "factors": factors,
#                 "number_of_factors": len(factors),
#             },
#             "requested_at": str(datetime.now()),
#             "requesting_user": request.user.username
#         }
#         return Response(
#             resp,
#             status=status.HTTP_200_OK
#         )


# class RandomBinaryNumber(APIView):
#     '''
#     API to generate a random binary number
#     '''
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         number_of_bits = int(request.query_params.get('bits', 10))
#         binary_number = Binary.random_binary_number(number_of_bits)

#         resp = {
#             "binary_number": binary_number,
#             "lenght": len(binary_number),
#             "requesting_user": request.user.username
#         }
#         return Response(
#             resp,
#             status=status.HTTP_200_OK
#         )


# class BinaryToInt(APIView):
#     '''
#     API to convert a binary number to an integer
#     '''
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         binary_number = int(request.query_params.get('binary_number', 0))
#         integer = Binary.binary_to_int(binary_number)

#         resp = {
#             "integer": integer,
#             "requesting_user": request.user.username
#         }
#         return Response(
#             resp,
#             status=status.HTTP_200_OK
#         )


# class IntToBinary(APIView):
#     '''
#     API to convert an integer to a binary number
#     '''
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         integer = int(request.query_params.get('integer', 0))
#         binary_number = Binary.int_to_binary(integer)

#         resp = {
#             "binary_number": binary_number,
#             "requesting_user": request.user.username
#         }
#         return Response(
#             resp,
#             status=status.HTTP_200_OK
#         )

'''
Microservice-based API Views.
'''


class FindPrimesInRangeView(APIView):
    '''
    API to find all Prime numbers in a given range
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = "prime_list"

    def get(self, request):

        params = request.query_params.get('upper_limit', 0)
        resp = GoAPIHandler.make_request(task=self.task, param=params)

        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class FindFactors(APIView):
    '''
    API to find all factors of a given number
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = "find_factors"

    def get(self, request):
        params = request.query_params.get('num', 0)
        resp = GoAPIHandler.make_request(task=self.task, param=params)
        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class RandomBinaryNumber(APIView):
    '''
    API to generate a random binary number
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = "random_binary"

    def get(self, request):
        params = request.query_params.get('bits', 0)
        resp = GoAPIHandler.make_request(task=self.task, param=params)

        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class BinaryToInt(APIView):
    '''
    API to convert a binary number to an integer
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = "binary_to_int"

    def get(self, request):
        params = request.query_params.get('binary_number', 0)
        resp = GoAPIHandler.make_request(task=self.task, param=params)

        return Response(
            resp,
            status=status.HTTP_200_OK
        )


class IntToBinary(APIView):
    '''
    API to convert an integer to a binary number
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = "int_to_binary"

    def get(self, request):
        params = request.query_params.get('num', 0)
        resp = GoAPIHandler.make_request(task=self.task, param=params)
        return Response(
            resp,
            status=status.HTTP_200_OK
        )
