# Generated by Django 4.0.5 on 2022-06-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_parts_options_alter_parts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
