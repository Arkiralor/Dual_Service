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
        verbose_name = 'Prime Number'
        verbose_name_plural = 'Prime Numbers'

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
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')
        verbose_name = 'Factor'
        verbose_name_plural = 'Factors'

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
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')
        verbose_name = 'Prime Factor'
        verbose_name_plural = 'Prime Factors'

    def __str__(self):
        return f"{self.function}"


class IntToBinaryModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_inttobin_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = models.CharField(max_length=256)

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'result', 'query')
        verbose_name = 'Int to Binary'
        verbose_name_plural = 'Int to Binaries'

    def __str__(self):
        return f"{self.function}"


class BinaryToIntModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_bintoint_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = models.CharField(max_length=256)

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'result', 'query')
        verbose_name = 'Binary to Int'
        verbose_name_plural = 'Binary to Integers'

    def __str__(self):
        return f"{self.function}"


class FibonacciModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_fibonacci_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    query = models.IntegerField()
    result = ArrayField(
        models.CharField(max_length=256),
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'query')
        verbose_name = 'Fibonacci Sequence'
        verbose_name_plural = 'Fibonacci Sequences'

    def __str__(self):
        return f"{self.function}"


class ArithSeriesModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_arith_series_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    start = models.IntegerField(default=0)
    terms = models.IntegerField(default=0)
    cd = models.IntegerField(default=0)
    result = ArrayField(
        models.CharField(max_length=256),
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'start', 'terms', 'cd')
        verbose_name = 'Arithmetic Series'
        verbose_name_plural = 'Arithmetic Series'

    def __str__(self):
        return f"{self.function}"


class GeoSeriesModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_geo_series_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    start = models.FloatField(default=0)
    terms = models.IntegerField(default=0)
    cr = models.FloatField(default=0)
    result = ArrayField(
        models.CharField(max_length=256),
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'start', 'terms', 'cr')
        verbose_name = 'Geometric Series'
        verbose_name_plural = 'Geometric Series'
        

    def __str__(self):
        return f"{self.function}"


class ProjectilePath2DModel(models.Model):
    requested_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='last_projectile_2d_requester', null=True)
    requested_at = models.DateTimeField(auto_now=True)
    function = models.CharField(max_length=256)
    length = models.IntegerField(blank=True, null=True)
    launch_angle = models.FloatField(default=0)
    launch_height = models.FloatField(default=0)
    launch_velocity = models.FloatField(default=0)
    result = ArrayField(
        models.JSONField(),
        size=8191,
    )

    class Meta:
        ordering = ['-requested_at']
        unique_together = ('function', 'launch_angle', 'launch_height', 'launch_velocity')
        verbose_name = '2D Projectile Path'
        verbose_name_plural = '2D Projectile Paths'

    def __str__(self):
        return f"{self.function}"


