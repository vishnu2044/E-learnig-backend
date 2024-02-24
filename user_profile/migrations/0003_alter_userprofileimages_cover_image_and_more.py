# Generated by Django 5.0 on 2024-02-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0002_alter_userprofileimages_cover_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofileimages",
            name="cover_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="user_cover_images/"
            ),
        ),
        migrations.AlterField(
            model_name="userprofileimages",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="user_profile_images/"
            ),
        ),
    ]