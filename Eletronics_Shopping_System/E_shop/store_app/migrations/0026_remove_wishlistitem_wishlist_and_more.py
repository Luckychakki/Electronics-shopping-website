# Generated by Django 5.1.2 on 2024-11-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0025_alter_filter_price_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitem',
            name='wishlist',
        ),
        migrations.RemoveField(
            model_name='wishlistitem',
            name='product',
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('30000 TO 40000', '30000 TO 40000'), ('20000 TO 30000', '20000 TO 30000'), ('1000 TO 10000', '1000 TO 10000'), ('10000 TO 20000', '10000 TO 20000'), ('40000 TO 50000', '40000 TO 50000')], max_length=60),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
        migrations.DeleteModel(
            name='WishlistItem',
        ),
    ]
