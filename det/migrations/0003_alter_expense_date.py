# Generated by Django 4.2.7 on 2023-12-28 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('det', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 28, 15, 54, 38, 131896, tzinfo=datetime.timezone.utc)),
        ),
    ]
