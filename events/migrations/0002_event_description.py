# Generated by Django 2.0.2 on 2018-02-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Kult'),
            preserve_default=False,
        ),
    ]