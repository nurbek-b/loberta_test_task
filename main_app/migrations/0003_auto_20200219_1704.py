# Generated by Django 2.2.8 on 2020-02-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200219_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(help_text='Enter your url', max_length=255)),
                ('check', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
