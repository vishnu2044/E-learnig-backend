# Generated by Django 5.0 on 2024-02-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EducationOptions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("education", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Professions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("profession", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]