# Generated by Django 5.1.2 on 2024-10-30 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_contact_us_alter_filter_price_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('1000 TO 10000', '1000 TO 10000'), ('10000 TO 20000', '10000 TO 20000'), ('20000 TO 30000', '20000 TO 30000'), ('40000 TO 50000', '40000 TO 50000'), ('30000 TO 40000', '30000 TO 40000')], max_length=60),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('additional_info', models.TextField()),
                ('amount', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='Product_images/Order_img')),
                ('quantity', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=15)),
                ('total', models.CharField(max_length=1000)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.order')),
            ],
        ),
    ]