# Generated by Django 4.1.1 on 2022-11-21 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_program_programfullimage_alter_program_programimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="programFullImage",
            field=models.ImageField(
                null=True, upload_to="djangouploads/programlar/images"
            ),
        ),
    ]
