# Generated by Django 4.1.4 on 2022-12-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, unique=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='storefront.category', verbose_name='دسته بندی'),
        ),
    ]
