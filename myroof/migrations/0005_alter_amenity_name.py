# Generated by Django 4.2 on 2023-05-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myroof", "0004_remove_complex_image_url_complex_images_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="amenity",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
