# Generated by Django 2.1.2 on 2018-10-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_person_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='telefone'),
        ),
    ]
