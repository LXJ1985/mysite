# Generated by Django 2.0 on 2018-05-27 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('read_statistics', '0002_readdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReadDetails',
            new_name='ReadDetail',
        ),
    ]
