# Generated by Django 4.0 on 2023-08-13 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0004_alter_start_star'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Start',
            new_name='Star',
        ),
    ]
