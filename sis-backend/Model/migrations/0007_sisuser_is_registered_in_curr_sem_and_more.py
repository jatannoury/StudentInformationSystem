# Generated by Django 4.1 on 2022-08-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0006_sisuser_admin_allows_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='sisuser',
            name='is_registered_in_curr_sem',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sisuser',
            name='student_status',
            field=models.CharField(default='Not Registered', max_length=20),
        ),
    ]
