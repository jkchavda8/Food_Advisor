# Generated by Django 5.0.2 on 2024-02-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_remove_target_tr_vitamin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='target',
            name='tr_vitamins',
            field=models.ManyToManyField(choices=[('A', 'vitamin A'), ('C', 'vitamin C'), ('D', 'vitamin D'), ('E', 'vitamin E'), ('K', 'vitamin K'), ('B1', 'thiamine'), ('B2', 'riboflavin'), ('B3', 'niacin'), ('B6', 'pyridoxine'), ('B12', 'cyanocobalamin'), ('B5', 'Pantothenic acid'), ('B7', 'Biotin '), ('B9', 'Folate')], to='first_app.vitamin'),
        ),
    ]
