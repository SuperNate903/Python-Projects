# Generated by Django 4.1.3 on 2022-11-25 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universitycampus',
            old_name='name',
            new_name='title',
        ),
    ]
