# Generated by Django 5.0.1 on 2024-02-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_eaten'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='quentity',
        ),
        migrations.AddField(
            model_name='report',
            name='consumed_items',
            field=models.CharField(default='jk', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='total_ingredient',
            field=models.CharField(default='not', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='total_vitamins',
            field=models.CharField(default='no', max_length=200),
            preserve_default=False,
        ),
    ]
