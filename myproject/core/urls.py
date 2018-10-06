from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('person/json/', v.person_json, name='person_json'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('cities/ajax/', v.cities_ajax, name='cities_ajax'),
    path(
        'cities/choices/ajax/',
        v.cities_choices_ajax,
        name='cities_choices_ajax'
    ),
    path('districts/ajax/', v.districts_ajax, name='districts_ajax'),
    path(
        'districts/choices/ajax/',
        v.districts_choices_ajax,
        name='districts_choices_ajax'
    ),
]
