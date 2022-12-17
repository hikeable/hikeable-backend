# Generated by Django 4.1.3 on 2022-12-17 07:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_trailmessage_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailmessage',
            name='likes',
        ),
        migrations.CreateModel(
            name='TrailMessageLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('create_date', models.DateField()),
                ('update_date', models.DateField(null=True)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.trailmessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.account')),
            ],
        ),
    ]
