# Generated by Django 5.1.2 on 2024-10-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_alter_filter_price_price_alter_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('40000 TO 50000', '40000 TO 50000'), ('1000 TO 10000', '1000 TO 10000'), ('20000 TO 30000', '20000 TO 30000'), ('30000 TO 40000', '30000 TO 40000'), ('10000 TO 20000', '10000 TO 20000')], max_length=60),
        ),
    ]
