# Generated by Django 3.0.5 on 2020-04-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200423_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mockset',
            name='msnumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
