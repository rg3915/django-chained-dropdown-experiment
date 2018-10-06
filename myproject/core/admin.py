from django.contrib import admin
from .models import Person, City, District


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('gender',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uf')
    search_fields = ('name', )
    list_filter = ('uf',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
