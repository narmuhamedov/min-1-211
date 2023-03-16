from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    title_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title_tag


class ProductForMedicine(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    name_product = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name_product

class Order(models.Model):
    STATUS = (
        ('На обработке', "На обработке"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен")
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductForMedicine, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
