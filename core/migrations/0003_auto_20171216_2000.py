# Generated by Django 2.0 on 2017-12-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171214_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_id', models.IntegerField()),
                ('done', models.BooleanField(default=0)),
                ('experiment', models.ForeignKey(on_delete=True, to='core.Experiment')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='experiment',
        ),
        migrations.AddField(
            model_name='event',
            name='sequence',
            field=models.ForeignKey(default=0, on_delete=True, to='core.Sequence'),
            preserve_default=False,
        ),
    ]