# Generated by Django 3.1.5 on 2021-03-24 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_information', '0005_gmail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outlook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_password', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_host', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_type', models.CharField(default='Enable SSL', max_length=255)),
                ('IMAP_port', models.IntegerField(blank=True, null=True)),
                ('smtp_host', models.CharField(blank=True, max_length=255, null=True)),
                ('smtp_port', models.IntegerField(blank=True, null=True)),
                ('smtp_password', models.CharField(blank=True, max_length=255, null=True)),
                ('smtp_type', models.CharField(default='STARTTLS', max_length=255)),
                ('emails_per_day', models.IntegerField(default=500)),
                ('daily_limit_left', models.IntegerField(default=-1)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtpemail', models.EmailField(max_length=254)),
                ('imapemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('smtpusername', models.CharField(blank=True, max_length=255, null=True)),
                ('imapusername', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_password', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_host', models.CharField(blank=True, max_length=255, null=True)),
                ('IMAP_type', models.CharField(default='Enable SSL', max_length=255)),
                ('IMAP_port', models.IntegerField(blank=True, null=True)),
                ('smtp_host', models.CharField(blank=True, max_length=255, null=True)),
                ('smtp_port', models.IntegerField(blank=True, null=True)),
                ('smtp_password', models.CharField(blank=True, max_length=255, null=True)),
                ('smtp_type', models.CharField(default='STARTTLS', max_length=255)),
                ('emails_per_day', models.IntegerField(default=500)),
                ('daily_limit_left', models.IntegerField(default=-1)),
                ('active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
