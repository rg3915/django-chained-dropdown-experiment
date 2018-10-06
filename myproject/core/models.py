from django.db import models


class Person(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=11, null=True, blank=True)
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
