from django.contrib import admin
from .models import UserData, Property, Building, Amenity, Complex, Address

admin.site.register(UserData)
admin.site.register(Property)
admin.site.register(Building)
admin.site.register(Address)
admin.site.register(Amenity)
admin.site.register(Complex)
