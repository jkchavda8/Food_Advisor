# Generated by Django 5.0.1 on 2024-02-29 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_remove_report_quentity_report_consumed_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_calories', models.IntegerField()),
                ('tr_vitamin', models.CharField(choices=[('A', 'vitamin A'), ('C', 'vitamin C'), ('D', 'vitamin D'), ('E', 'vitamin E'), ('K', 'vitamin K'), ('B1', 'thiamine'), ('B2', 'riboflavin'), ('B3', 'niacin'), ('B6', 'pyridoxine'), ('B12', 'cyanocobalamin'), ('B5', 'Pantothenic acid'), ('B7', 'Biotin '), ('B9', 'Folate')], max_length=10)),
                ('tr_ingredient', models.CharField(max_length=100)),
                ('pr_nm', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='first_app.person')),
            ],
        ),
    ]
