# Generated by Django 4.0 on 2022-06-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_items_orderitem_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
