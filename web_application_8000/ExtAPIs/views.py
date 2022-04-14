from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExtAPIs.external_api_handler import GoAPIHandler
from globalconstants.global_constants import GoAPITasks

'''
Microservice-based API Views.
'''


class FindPrimesInRangeView(APIView):
    '''
    API to find all Prime numbers in a given range
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = GoAPITasks.PRIMES

    def get(self, request):

        params = request.query_params.get('upper_limit', 0)
        resp = GoAPIHandler.dispatch(task=self.task, query=params)

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
    task = GoAPITasks.FACTORS

    def get(self, request):
        params = request.query_params.get('num', 0)
        resp = GoAPIHandler.dispatch(task=self.task, query=params)
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
    task = GoAPITasks.RANDOM_BINARY

    def get(self, request):
        params = request.query_params.get('bits', 0)
        resp = GoAPIHandler.dispatch(task=self.task, query=params)

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
    task = GoAPITasks.BINARY_TO_INT

    def get(self, request):
        params = request.query_params.get('binary_number', 0)
        resp = GoAPIHandler.dispatch(task=self.task, query=params)

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
    task = GoAPITasks.INT_TO_BINARY
    def get(self, request):
        params = request.query_params.get('num', 0)
        resp = GoAPIHandler.dispatch(task=self.task, query=params)
        return Response(
            resp,
            status=status.HTTP_200_OK
        )
