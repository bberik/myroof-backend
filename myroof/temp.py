from .models import Building, Property
from django.forms.models import model_to_dict

# Get all the Building instances
buildings = Building.objects.all()[1:]

# Loop through each building
for building in buildings:
    # Loop through 5 times to create 5 properties for each building
    for i in range(5):
        original_property = Property.objects.get(id=i+1)
        new_property = Property(**model_to_dict(original_property, exclude=['id']))
        new_building = building  # Replace with the ID of the new Building instance
        new_property.building = new_building
        new_property.save()

