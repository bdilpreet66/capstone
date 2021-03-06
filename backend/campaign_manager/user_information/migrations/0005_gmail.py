# Generated by Django 3.1.5 on 2021-03-22 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_information', '0004_auto_20210322_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('key', models.CharField(max_length=255)),
                ('emails_per_day', models.IntegerField(default=400)),
                ('daily_limit_left', models.IntegerField(default=400)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
