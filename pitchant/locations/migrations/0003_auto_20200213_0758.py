# Generated by Django 3.0.3 on 2020-02-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_code',
            field=models.CharField(max_length=20),
        ),
    ]
