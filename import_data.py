import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

import names
import string
from random import choice
from django.utils.text import slugify
from myproject.core.models import Person, City, District


City.objects.all().delete()
District.objects.all().delete()

cities = []
with open('fix/cities.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        city = City(name=row['name'], uf=row['uf'])
        cities.append(city)

City.objects.bulk_create(cities)


districts = []
with open('fix/districts.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        city = City.objects.get(name=row['city'])
        district = District(name=row['name'], city=city)
        districts.append(district)

District.objects.bulk_create(districts)


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


districts = District.objects.all()
districts_list = []

for district in districts:
    for _ in range(7):
        name = names.get_full_name()
        email = slugify(name) + '@email.com'
        phone = gen_digits(11)
        data = dict(name=name, email=email, phone=phone, district=district)
        districts_list.append(Person(**data))
        print(Person(**data))

Person.objects.bulk_create(districts_list)
