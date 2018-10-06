from django.shortcuts import render
from django.http import JsonResponse
from localflavor.br.br_states import STATE_CHOICES
from .models import Person, City, District


def index(request):
    context = {}
    person_list = Person.objects.all()
    context['person_list'] = person_list
    return render(request, 'index.html', context)


def person_json(request):
    persons = Person.objects.all()
    data = [person.to_dict_json() for person in persons]
    response = {'data': data}
    return JsonResponse(response)


def dashboard(request):
    context = {}
    cities = City.objects.all()
    districts = District.objects.all()
    context['states'] = STATE_CHOICES
    # context['states'] = (
    #     ('MG', 'Minas Gerais'),
    #     ('PR', 'Paraná'),
    #     ('RJ', 'Rio de Janeiro'),
    #     ('SP', 'São Paulo'),
    # )
    context['cities'] = cities
    context['districts'] = districts
    return render(request, 'dashboard.html', context)
