# Generated by Django 5.1.1 on 2024-09-16 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_product_seasonal_event_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='alternative_text',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='name',
        ),
        migrations.AddField(
            model_name='productimage',
            name='alt_text',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter a category...', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.producttype'),
        ),
    ]
