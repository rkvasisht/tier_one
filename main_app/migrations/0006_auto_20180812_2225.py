# Generated by Django 2.0.7 on 2018-08-12 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_pushedworkout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pushedworkout',
            old_name='Workouts',
            new_name='workouts',
        ),
    ]