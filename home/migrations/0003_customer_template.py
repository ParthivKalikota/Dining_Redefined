# Generated by Django 5.1.3 on 2024-11-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_about_customer_email_customer_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='template',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]