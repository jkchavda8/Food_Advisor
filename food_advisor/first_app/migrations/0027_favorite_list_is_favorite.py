# Generated by Django 5.0.2 on 2024-03-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0026_eaten_date_alter_report_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite_list',
            name='is_favorite',
            field=models.BooleanField(default=True),
        ),
    ]
