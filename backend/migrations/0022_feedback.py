# Generated by Django 4.1.3 on 2022-12-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_trailcomment_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_name', models.CharField(max_length=255)),
                ('from_email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]