# Generated by Django 4.1.3 on 2023-10-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customusersb",
            name="about_me",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="customusersb",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
    ]