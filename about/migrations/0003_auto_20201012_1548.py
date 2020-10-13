# Generated by Django 3.1.2 on 2020-10-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20201012_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='description',
            new_name='description1',
        ),
        migrations.AddField(
            model_name='index',
            name='description12',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='index',
            name='jobtitle',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AddField(
            model_name='index',
            name='name',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='index',
            name='cta',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='index',
            name='heading',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]