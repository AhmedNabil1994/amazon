# Generated by Django 4.0.1 on 2022-02-04 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_track_alter_myusers_userpassword_trainee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='track_name',
            new_name='track_id',
        ),
    ]
