from django.contrib import admin
from user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()
    filter_vertical = ()
    fieldsets = ()
