# Generated by Django 4.2.7 on 2024-01-03 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('det', '0004_alter_expense_date_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 1, 3, 15, 12, 34, 228084, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
