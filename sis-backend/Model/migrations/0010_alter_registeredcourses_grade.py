# Generated by Django 4.1 on 2022-08-29 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0009_rename_instructor_id_registeredcourses_instructor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredcourses',
            name='grade',
            field=models.FloatField(default='0.00', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)]),
        ),
    ]
