# Generated by Django 5.1.2 on 2024-11-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='About',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_no',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
