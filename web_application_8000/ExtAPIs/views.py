from django.db import models

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExtAPIs.models import Prime, Factor, PrimeFactorModel, IntToBinaryModel, BinaryToIntModel, RandomBinary, \
    FibonacciModel, ArithSeriesModel, GeoSeriesModel
from ExtAPIs.serializers import PrimeSerializer, FactorSerializer, PrimeFactorSerializer, IntToBinarySerializer,\
    BinaryToIntSerializer, RandomBinarySerializer, FibonacciSerializer, ArithSeriesSerializer, GeoSeriesSerializer
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


class PrimeFactorView(APIView):
    '''
    API to find the prime factors of a given number.
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = GoAPITasks.PRIME_FACTORS

    def get(self, request):
        params = request.query_params.get('num', 0)
        qryset = PrimeFactorModel.objects.filter(query = params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = PrimeFactorSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = PrimeFactorSerializer(qryset)
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


class FibonacciView(APIView):
    '''
    API to find 'n' terms of the Fibonacci Sequence
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = GoAPITasks.FIBONACCI

    def get(self, request):
        params = request.query_params.get('terms', 0)
        qryset = FibonacciModel.objects.filter(query=params).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = FibonacciSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = FibonacciSerializer(qryset)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )


class RegArithSeriesView(APIView):
    '''
    API to find 'n' terms of a Regular Arithmetic Series
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = GoAPITasks.REG_ARITH_SERIES

    def get(self, request):
        start = request.query_params.get('start', 0)
        terms = request.query_params.get('terms', 0)
        cd = request.query_params.get('cd', 0)
        params = {
            'start': start,
            'terms': terms,
            'cd': cd
        }
        qryset = ArithSeriesModel.objects.filter(
            models.Q(start=start) 
            and models.Q(terms=terms) 
            and models.Q(cd=cd)
        ).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = ArithSeriesSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = ArithSeriesSerializer(qryset)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )


class RegGeoSeriesView(APIView):
    '''
    API to find 'n' terms of a Regular Geometric Series
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    task = GoAPITasks.REG_GEO_SERIES

    def get(self, request):
        start = request.query_params.get('start', 0)
        terms = request.query_params.get('terms', 0)
        cr = request.query_params.get('cr', 0)
        params = {
            'start': start,
            'terms': terms,
            'cr': cr
        }
        qryset = GeoSeriesModel.objects.filter(
            models.Q(start=start) 
            and models.Q(terms=terms) 
            and models.Q(cr=cr)
        ).first()
        if not qryset:
            resp = GoAPIHandler.dispatch(task=self.task, query=params)
            resp['requested_by'] = request.user.id
            if resp.get('length') > 8191:
                resp['result'] = resp.get('result')[:8190]
                resp['function'] = resp.get('function') + ' (truncated till [8190])'
            new_qryset = GeoSeriesSerializer(data=resp)
            if new_qryset.is_valid():
                new_qryset.save()
                return Response(new_qryset.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    new_qryset.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                    )
        serialized = GeoSeriesSerializer(qryset)
        return Response(
            serialized.data,
            status=status.HTTP_200_OK
        )
