# Generated by Django 5.0.6 on 2024-10-22 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_tutor_delete_customuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tutor",
            name="hours_per_day",
        ),
    ]