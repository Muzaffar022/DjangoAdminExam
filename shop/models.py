from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.title


verbose_name_plural = Company


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Sale(models.Model):
    consumer = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
