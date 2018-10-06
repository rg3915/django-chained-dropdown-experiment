from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('gender',)
