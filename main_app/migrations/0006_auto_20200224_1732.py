# Generated by Django 2.2.8 on 2020-02-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_url_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
