# Generated by Django 2.2.17 on 2021-03-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0020_auto_20210225_1544"),
    ]

    operations = [
        migrations.DeleteModel(name="LocalizedSMSMessage"),
    ]