# Generated by Django 2.2.20 on 2021-06-03 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0008_reportcache'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphitevariable',
            name='period',
            field=models.CharField(default='', max_length=12),
        ),
    ]