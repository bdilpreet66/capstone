# Generated by Django 3.1.5 on 2021-03-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contactlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlist',
            name='contact',
            field=models.ManyToManyField(blank=True, to='contacts.Contact'),
        ),
    ]