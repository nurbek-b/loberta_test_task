# Generated by Django 2.2.8 on 2020-02-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200219_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status',
            field=models.IntegerField(max_length=3, null=True),
        ),
    ]
