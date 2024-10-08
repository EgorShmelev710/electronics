# Generated by Django 5.1 on 2024-08-23 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='NetworkEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='network.contactinfo', verbose_name='контакты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='network.networkentity', verbose_name='поставщик')),
                ('products', models.ManyToManyField(to='network.product')),
            ],
            options={
                'verbose_name': 'звено сети',
                'verbose_name_plural': 'звенья сети',
            },
        ),
    ]
