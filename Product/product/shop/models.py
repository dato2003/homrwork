from django.db import models


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    quality = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class LoyalCustomer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    favorite_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='loyal_customers'
    )

    def __str__(self):
        return self.name
