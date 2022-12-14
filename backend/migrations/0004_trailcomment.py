# Generated by Django 4.1.3 on 2022-12-03 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_trail_length_alter_trail_map_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=10000)),
                ('date', models.DateField()),
                ('trail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.trail')),
            ],
        ),
    ]
