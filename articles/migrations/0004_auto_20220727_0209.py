# Generated by Django 4.0.6 on 2022-07-27 02:09

from django.db import migrations


def populate_status(apps, schemaeditor):
    statuses = {
        "published": "Content that is on the site.",
        "pending":  "Content not yet edited.",
        "revision": "needs revisions",
        "denied": "Denied.  You Suck.",
        "in progres":  "in progress",
    }
    Status = apps.get_model("articles", "Status")
    for name, desc in statuses.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_status_article_status'),
    ]

    operations = [
    ]