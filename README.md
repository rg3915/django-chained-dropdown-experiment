# django-chained-dropdown-experiment

Experiment chained dropdown list with Django.

Video no [YouTube]()

## Como rodar este projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-chained-dropdown-experiment.git
cd django-chained-dropdown-experiment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Tutorial

Vamos começar com base no projeto [django-datatables-experiment](https://github.com/rg3915/django-datatables-experiment).

```
git clone https://github.com/rg3915/django-datatables-experiment.git
```

A partir dai assista o video no [YouTube]().

### Anotações mostradas no video:

#### Copiando arquivos

```
cp -r django-datatables-experiment/contrib/ .
cp -r django-datatables-experiment/myproject/ .
cp django-datatables-experiment/manage.py .
cp django-datatables-experiment/requirements.txt .
cp django-datatables-experiment/.gitignore .
rm -rf django-datatables-experiment/
```

#### Iniciando o projeto

```
python -V
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username='admin'
```

#### Resetando a senha

```python
python manage.py shell_plus
user = User.objects.get(username='admin')
user.set_password('d')
user.save()
exit()
```

#### Importando os dados

```
mkdir fix
cd fix
wget 
wget 
python import_data.py
```

#### Lendo os dados

```python
python manage.py shell_plus
City.objects.all()
City.objects.all().count()
Distric.objects.last()
Distric.objects.all().count()
```


### Referências

[How to Implement Dependent/Chained Dropdown List with Django](https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html)

https://django-localflavor.readthedocs.io/en/latest/localflavor/br/
