# Generated by Django 2.2.20 on 2021-05-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0005_auto_20210526_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphitevariable',
            name='function',
            field=models.CharField(choices=[('A', 'avg'), ('MA', 'max'), ('MI', 'min')], default='A', max_length=12),
        ),
    ]
