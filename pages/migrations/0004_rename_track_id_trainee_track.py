# Generated by Django 4.0.1 on 2022-02-04 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_track_name_trainee_track_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='track_id',
            new_name='track',
        ),
    ]
