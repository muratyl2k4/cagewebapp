# Generated by Django 4.1.1 on 2022-10-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_program_delete_programlar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="programTitle",
            field=models.SlugField(max_length=150),
        ),
    ]