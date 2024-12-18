# Generated by Django 5.1.2 on 2024-11-01 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0019_alter_filter_price_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('20000 TO 30000', '20000 TO 30000'), ('40000 TO 50000', '40000 TO 50000'), ('1000 TO 10000', '1000 TO 10000'), ('10000 TO 20000', '10000 TO 20000'), ('30000 TO 40000', '30000 TO 40000')], max_length=60),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store_app.wishlist')),
            ],
        ),
    ]
