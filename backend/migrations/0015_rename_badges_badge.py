# Generated by Django 4.1.3 on 2022-12-13 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_badges'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Badges',
            new_name='Badge',
        ),
    ]
