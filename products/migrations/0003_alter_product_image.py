# Generated by Django 4.2 on 2024-09-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_options_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="default_image.jpeg", upload_to="uploads/"),
        ),
    ]
