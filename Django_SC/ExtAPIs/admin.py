from django.contrib import admin
from ExtAPIs.models import Prime, Factor, PrimeFactorModel, IntToBinaryModel, BinaryToIntModel,\
    FibonacciModel, ArithSeriesModel, GeoSeriesModel, ProjectilePath2DModel
# Register your models here.


@admin.register(Prime)
class PrimeAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(Factor)
class FactorAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50

@admin.register(PrimeFactorModel)
class PrimeFactorAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(IntToBinaryModel)
class IntToBinaryAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(BinaryToIntModel)
class BinaryToIntAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(FibonacciModel)
class FibonacciAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(ArithSeriesModel)
class ArithSeriesAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'start', 'terms', 'cd')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'start', 'terms', 'cd']
    list_per_page = 50


@admin.register(GeoSeriesModel)
class GeoSeriesAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'start', 'terms', 'cr')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'start', 'terms', 'cr']
    list_per_page = 50


@admin.register(ProjectilePath2DModel)
class ProjectilePath2DAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'launch_angle', 'launch_velocity', 'launch_height')
    raw_id_fields = ('requested_by',)
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'launch_angle', 'launc_velocity', 'launch_height']
    list_per_page = 50
