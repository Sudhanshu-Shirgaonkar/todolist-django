# Generated by Django 4.1.6 on 2023-02-01 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="task", options={"ordering": ["complete"]},),
        migrations.AddField(
            model_name="task",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
