# Generated by Django 4.2.4 on 2023-08-11 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homemotto',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='homemotto',
            name='title2',
        ),
    ]