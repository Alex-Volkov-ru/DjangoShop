# Generated by Django 5.0.3 on 2024-04-07 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_rename_poducts_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
