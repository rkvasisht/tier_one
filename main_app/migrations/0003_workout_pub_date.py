# Generated by Django 2.0.7 on 2018-08-12 00:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_excercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]