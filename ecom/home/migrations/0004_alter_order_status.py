# Generated by Django 4.2.1 on 2023-07-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tag_order_customer_order_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('OUT FOR DELIVERY', 'OUT FOR DELIVERY'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
