# Generated by Django 4.1.2 on 2022-12-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("teacher_name", models.CharField(max_length=200)),
                ("teacher_email", models.CharField(max_length=200)),
                ("teacher_phone", models.IntegerField()),
                ("teacher_joining", models.DateField()),
                ("teacher_education", models.CharField(max_length=200)),
                ("teacher_id", models.CharField(max_length=200)),
                ("teacher_work_exp", models.CharField(max_length=200)),
                ("teacher_packeg", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]