from django.db import models
# Create your models here.


class Mobiles(models.Model):
    mobile_name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images", null=True)
    RAM_ROM = models.CharField(max_length=120)
    processor = models.CharField(max_length=50)
    rear_camera = models.CharField(max_length=50)
    front_camera = models.CharField(max_length=50)
    battery = models.CharField(max_length=50, null=True)
    display = models.CharField(max_length=120)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.mobile_name

    @property
    def m_reviews(self):
        return self.reviews.all()