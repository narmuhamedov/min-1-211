# Generated by Django 4.1.2 on 2023-03-16 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("phone", models.CharField(max_length=200)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("title_tag", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ProductForMedicine",
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
                ("name_product", models.CharField(max_length=100)),
                ("price", models.PositiveIntegerField()),
                ("description", models.TextField(blank=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("tags", models.ManyToManyField(to="drugstor.tag")),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("На обработке", "На обработке"),
                            ("Выехал", "Выехал"),
                            ("Доставлен", "Доставлен"),
                        ],
                        max_length=100,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drugstor.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="drugstor.productformedicine",
                    ),
                ),
            ],
        ),
    ]