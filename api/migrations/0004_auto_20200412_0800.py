# Generated by Django 3.0.5 on 2020-04-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200412_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(default='', max_length=100, verbose_name='destination'),
        ),
    ]