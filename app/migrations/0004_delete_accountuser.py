# Generated by Django 4.0.3 on 2022-07-14 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_accountuser_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accountuser',
        ),
    ]
