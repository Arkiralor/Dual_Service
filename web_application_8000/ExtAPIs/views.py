from ctypes import sizeof
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExtAPIs.models import Prime, Factor, IntToBinaryModel, BinaryToIntModel, RandomBinary
from ExtAPIs.serializers import PrimeSerializer, FactorSerializer, IntToBinarySerializer,\
    BinaryToIntSerializer, RandomBinarySerializer
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
        qryset = Prime.objects.filter(query=params).first()

        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = PrimeSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = PrimeSerializer(qryset)
        return Response(
            serialized.data,
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
        qryset = Factor.objects.filter(query=params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = FactorSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = FactorSerializer(qryset)
        return Response(
            serialized.data,
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
        qryset = RandomBinary.objects.filter(query=params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            new_qryset = RandomBinarySerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = RandomBinarySerializer(qryset)
        return Response(
            serialized.data,
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
        qryset = BinaryToIntModel.objects.filter(query=params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            new_qryset = BinaryToIntSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = BinaryToIntSerializer(qryset)
        return Response(
            serialized.data,
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
        qryset = IntToBinaryModel.objects.filter(query=params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            new_qryset = IntToBinarySerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = IntToBinarySerializer(qryset)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )
