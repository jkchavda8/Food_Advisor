# Generated by Django 5.0.2 on 2024-02-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0019_alter_target_tr_vitamins_alter_vitamin_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='tr_vitamins',
        ),
        migrations.DeleteModel(
            name='Vitamin',
        ),
        migrations.AddField(
            model_name='target',
            name='tr_vitamins',
            field=models.CharField(choices=[('A', 'vitamin A'), ('C', 'vitamin C'), ('D', 'vitamin D'), ('E', 'vitamin E'), ('K', 'vitamin K'), ('B1', 'thiamine'), ('B2', 'riboflavin'), ('B3', 'niacin'), ('B6', 'pyridoxine'), ('B12', 'cyanocobalamin'), ('B5', 'Pantothenic acid'), ('B7', 'Biotin '), ('B9', 'Folate')], default='f', max_length=100),
            preserve_default=False,
        ),
    ]