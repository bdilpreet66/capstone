# Generated by Django 3.1.5 on 2021-03-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_information', '0002_auto_20210310_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
    ]
