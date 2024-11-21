# Generated by Django 5.1.2 on 2024-10-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_remove_order_additional_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('10000 TO 20000', '10000 TO 20000'), ('1000 TO 10000', '1000 TO 10000'), ('20000 TO 30000', '20000 TO 30000'), ('30000 TO 40000', '30000 TO 40000'), ('40000 TO 50000', '40000 TO 50000')], max_length=60),
        ),
    ]
