# Generated by Django 5.1.7 on 2025-03-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_usercredentials_remove_payment_amount_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OTP",
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
                ("otp", models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
    ]
