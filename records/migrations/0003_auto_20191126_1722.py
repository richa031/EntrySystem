# Generated by Django 2.2.7 on 2019-11-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20191123_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='check_out',
        ),
        migrations.AddField(
            model_name='record',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
    ]