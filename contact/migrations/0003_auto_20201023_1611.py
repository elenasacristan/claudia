# Generated by Django 3.1.2 on 2020-10-23 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201013_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('date',), 'verbose_name_plural': 'Emails'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
