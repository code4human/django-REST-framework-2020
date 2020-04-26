# Generated by Django 3.0.5 on 2020-04-26 01:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200426_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='date_delivered',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='배송일자'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입일'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='주문일자'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supply_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='공급일자'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일자'),
        ),
    ]