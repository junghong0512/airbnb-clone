# Generated by Django 2.2.5 on 2020-07-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rooms',
            new_name='room',
        ),
    ]
