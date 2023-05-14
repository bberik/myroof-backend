# Generated by Django 4.2 on 2023-05-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myroof", "0002_address_amenity_building_property_contract_complex_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
