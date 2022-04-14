from django.contrib import admin
from ExtAPIs.models import Prime, Factor, IntToBinaryModel, BinaryToInt, RandomBinary

# Register your models here.


@admin.register(Prime)
class PrimeAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(Factor)
class FactorAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(IntToBinaryModel)
class IntToBinaryAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(BinaryToInt)
class BinaryToIntAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50


@admin.register(RandomBinary)
class RandomBinaryAdmin(admin.ModelAdmin):
    list_display = ('requested_by', 'requested_at', 'function',
                    'length', 'query', 'result')
    ordering = ['-requested_at']
    search_fields = ['function', 'result', 'query']
    list_per_page = 50
