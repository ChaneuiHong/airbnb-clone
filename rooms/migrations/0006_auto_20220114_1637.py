# Generated by Django 2.2.5 on 2022-01-14 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220109_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='isntant_book',
            new_name='instant_book',
        ),
    ]