# Generated by Django 4.2.10 on 2024-03-22 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apis_ontology", "0017_rename_lat_place_latitude_rename_lng_place_longitude"),
    ]

    operations = [
        migrations.RenameField(
            model_name="place",
            old_name="name",
            new_name="label",
        ),
    ]
