# Generated by Django 4.1.6 on 2023-02-01 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_alter_task_title_alter_task_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task", options={"ordering": ["complete", "-created"]},
        ),
        migrations.AddField(
            model_name="task",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
