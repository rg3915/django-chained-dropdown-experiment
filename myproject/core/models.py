from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Person(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=15, null=True, blank=True)
    GENDER = (
        ('0', ''),
        ('man', 'homem'),
        ('woman', 'mulher'),
    )
    gender = models.CharField(
        'sexo',
        max_length=5,
        choices=GENDER,
        default='0'
    )
    district = models.ForeignKey(
        'District',
        verbose_name='bairro',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'gender': self.get_gender_display(),
        }


class City(models.Model):
    name = models.CharField('cidade', max_length=100)
    uf = models.CharField('UF', max_length=2, choices=STATE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'cidade'
        verbose_name_plural = 'cidades'


class District(models.Model):
    name = models.CharField('distrito', max_length=100)
    city = models.ForeignKey(
        'City',
        verbose_name='cidade',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'distrito'
        verbose_name_plural = 'distritos'
