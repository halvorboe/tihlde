# Generated by Django 2.0 on 2018-02-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]