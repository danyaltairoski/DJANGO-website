# Generated by Django 4.2 on 2023-07-14 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio_app", "0003_rename_experience_workexperience"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="technologies",
        ),
    ]
