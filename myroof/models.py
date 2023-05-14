from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _




class UserData(AbstractUser):

    mobile = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =["username"]


ROOMS_CHOICES = [
    (1, "1 room"),
    (2, "2 rooms"),
    (3, "3 rooms"),
    (4, "4 rooms or more"),
]


# Create your models here.
class Amenity(models.Model):
    name = models.CharField(max_length=50)


class Address(models.Model):
    postal_code = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    building_number = models.CharField(max_length=10, default="NG")



class Complex(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    amenities = models.ManyToManyField("Amenity")
    date_built = models.DateField()
    constructor = models.ForeignKey(UserData, on_delete=models.PROTECT)
    website = models.CharField(max_length=50)
    images = models.CharField(max_length=1000, default='')

class Building(models.Model):
    name = models.CharField(max_length=50)
    floors = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    complex = models.ForeignKey(Complex, on_delete=models.PROTECT)


class Property(models.Model):
    name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, on_delete=models.PROTECT)
    property_type = models.CharField(max_length=20)
    owner = models.ForeignKey(UserData, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    floor = models.IntegerField()
    area = models.FloatField(default=0)
    rooms = models.IntegerField(choices=ROOMS_CHOICES)
    bathrooms = models.IntegerField(choices=ROOMS_CHOICES)
    amenities = models.ManyToManyField("Amenity")
    description = models.TextField(max_length=10000)
    images = models.CharField(max_length=1000, default="")


class Contract(models.Model):
    is_valid = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    review = models.JSONField()
    renter = models.ForeignKey(UserData, on_delete=models.PROTECT)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
