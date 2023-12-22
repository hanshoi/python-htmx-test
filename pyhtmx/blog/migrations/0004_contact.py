# Generated by Django 4.2.7 on 2023-11-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_remove_tag_blogs_blog_tags_alter_blog_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("email", models.CharField(max_length=128)),
                ("message", models.CharField(max_length=1080)),
            ],
        ),
    ]