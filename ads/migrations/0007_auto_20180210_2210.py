# Generated by Django 2.0 on 2018-02-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20180210_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='deadline',
            field=models.DateField(),
        ),
    ]
