# Generated by Django 5.0.5 on 2024-05-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_bug_log", "0007_remove_bug_urlhash"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bug",
            name="bug_id",
        ),
        migrations.AddField(
            model_name="bug",
            name="id",
            field=models.CharField(
                default=12345, max_length=20, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
    ]
