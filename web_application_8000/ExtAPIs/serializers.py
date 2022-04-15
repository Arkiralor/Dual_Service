from dataclasses import field
from rest_framework import serializers
from ExtAPIs.models import Prime, Factor, PrimeFactorModel, IntToBinaryModel, BinaryToIntModel, RandomBinary


class PrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prime
        fields = '__all__'


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = '__all__'


class PrimeFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimeFactorModel
        fields = '__all__'


class IntToBinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = IntToBinaryModel
        fields = '__all__'


class BinaryToIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinaryToIntModel
        fields = '__all__'


class RandomBinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomBinary
        fields = '__all__'
