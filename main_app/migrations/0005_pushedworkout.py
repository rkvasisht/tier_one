# Generated by Django 2.0.7 on 2018-08-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_workout_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushedWorkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Workouts', models.ManyToManyField(to='main_app.Workout')),
            ],
        ),
    ]
