# Generated by Django 3.0.7 on 2020-07-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200630_0735'),
        ('account', '0003_auto_20200702_1202'),
        ('order', '0002_auto_20200701_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartwishlist',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ProductColor'),
        ),
        migrations.AlterField(
            model_name='order',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Guest'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderStatus'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.IntegerField(),
        ),
    ]
