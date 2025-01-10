from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    image = models.URLField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="menu_items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ("Order Placed", "Order Placed"),
        ("Preparing", "Preparing"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.JSONField()  # Store item details as JSON
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Order Placed")
    delivery_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
