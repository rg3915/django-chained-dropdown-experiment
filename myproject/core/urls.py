from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('person/json/', v.person_json, name='person_json'),
    path('dashboard/', v.dashboard, name='dashboard'),
    path('cities/ajax/', v.cities_ajax, name='cities_ajax'),
]
