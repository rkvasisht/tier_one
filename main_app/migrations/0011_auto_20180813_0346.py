# Generated by Django 2.0.7 on 2018-08-13 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180813_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushedworkout',
            name='assigned',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pushedworkout',
            name='inclass',
            field=models.BooleanField(),
        ),
    ]
