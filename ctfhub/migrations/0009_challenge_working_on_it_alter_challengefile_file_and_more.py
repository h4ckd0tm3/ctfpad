# Generated by Django 4.2.2 on 2023-06-28 22:26

import ctfhub.helpers
import ctfhub.validators
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ctfhub", "0008_remove_challenge_whiteboard_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="working_on_it",
            field=models.ManyToManyField(
                blank=True, related_name="working_on_challenges", to="ctfhub.member"
            ),
        ),
        migrations.AlterField(
            model_name="challengefile",
            name="file",
            field=models.FileField(
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    base_url="/uploads/", location="/code/uploads"
                ),
                upload_to=ctfhub.helpers.get_challenge_upload_path,
                validators=[ctfhub.validators.challenge_file_max_size_validator],
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="avatar",
            field=models.ImageField(
                blank=True,
                storage=django.core.files.storage.FileSystemStorage(
                    base_url="/uploads/", location="/code/uploads"
                ),
                upload_to="media/",
            ),
        ),
    ]
