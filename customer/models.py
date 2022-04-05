from django.db import models
from owner.models import Mobiles
from django.contrib.auth.models import User
from datetime import timedelta, datetime
# Create your models here.


class Cart(models.Model):
    product = models.ForeignKey(Mobiles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    qty = models.PositiveIntegerField(default=1)
    options = (
        ("in_cart", "in_cart"),
        ("order_placed", "order_placed"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(max_length=20, choices=options, default="in_cart")


class Orders(models.Model):
    product = models.ForeignKey(Mobiles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    qty = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, null=True)
    d_date = datetime.today()+timedelta(days=5)
    expected_delivery_date = models.DateField(default=d_date, null=True)
    options = (
        ("orderplaced", "orderplaced"),
        ("dispatched", "dispatched"),
        ("in_transmit", "in_transmit"),
        ("delivered", "delivered"),
        ("order_cancelled", "order_cancelled")
    )
    status = models.CharField(max_length=20, choices=options, default="orderplaced")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    phone_no = models.CharField(max_length=12)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="images", null=True)