# Generated by Django 2.0 on 2017-12-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_experiment_is_trial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='first_ts',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='session',
            name='last_ts',
            field=models.FloatField(default=0),
        ),
    ]
