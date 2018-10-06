import csv
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()


from myproject.core.models import City, District


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
