# Generated by Django 4.2 on 2024-09-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-id"]},
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default="media/default_image.jpeg", upload_to=None),
        ),
    ]
