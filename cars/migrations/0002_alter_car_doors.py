# Generated by Django 4.0 on 2022-06-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]),
        ),
    ]