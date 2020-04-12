# Generated by Django 3.0.5 on 2020-04-11 21:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ('-date_joined',)},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='location',
            field=models.CharField(max_length=100, verbose_name='user address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(max_length=30, verbose_name="user's name"),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_num', models.AutoField(primary_key=True, serialize=False, verbose_name='number of product (PK)')),
                ('name', models.CharField(max_length=100, verbose_name='name of product')),
                ('inventory', models.IntegerField(verbose_name='inventory')),
                ('price', models.IntegerField(verbose_name='price of product')),
                ('supply_date', models.DateTimeField(verbose_name='supply date')),
                ('supply_vol', models.IntegerField(verbose_name='supply volume')),
                ('manu_name', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='api.Manufacturer', verbose_name='manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='pro_num',
            field=models.ForeignKey(default=0, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='api.Product', verbose_name='number of product'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('many', models.IntegerField(verbose_name='quantity ordered')),
                ('date_ordered', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date ordered')),
                ('message', models.CharField(blank=True, max_length=300, verbose_name='request message')),
                ('pro_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MyUser')),
            ],
            options={
                'unique_together': {('user_id', 'pro_num')},
            },
        ),
    ]