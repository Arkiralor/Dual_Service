from django.db import models
from django.contrib.postgres.fields import ArrayField

from user.models import User

# Create your models here.


class Prime(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_prime_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = ArrayField(
        models.IntegerField(),
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')

    def __str__(self):
        return f"{self.function}"


class Factor(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_factor_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = ArrayField(
        models.IntegerField(),
        size=4096,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')

    def __str__(self):
        return f"{self.function}"


class PrimeFactorModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_prime_factor_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = ArrayField(
        models.IntegerField(),
        size=4096,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')

    def __str__(self):
        return f"{self.function}"


class IntToBinaryModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_inttobin_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = models.IntegerField()

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'result', 'query')

    def __str__(self):
        return f"{self.function}"


class BinaryToIntModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_bintoint_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = models.IntegerField()

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'result', 'query')

    def __str__(self):
        return f"{self.function}"


class RandomBinary(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_randbin_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = models.IntegerField()

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'result', 'query')

    def __str__(self):
        return f"{self.function}"
