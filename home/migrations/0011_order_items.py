# Generated by Django 3.2.5 on 2022-06-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='home.OrderItem'),
        ),
    ]
