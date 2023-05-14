from rest_framework import serializers
from .models import UserData, Property, Building, Complex, Contract, Address, Amenity

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "username", "password", "first_name", "last_name", "mobile"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       username=validated_data['username'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'],
                                       mobile=validated_data['mobile'],

                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for Address model
    """

    class Meta:
        model = Address
        fields = ("street", "city", "postal_code", "building_number")


class UserDataSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """

    class Meta:
        model = UserData
        fields = (
            "username",
            "first_name",
            "last_name",
            "mobile",
            "email",
        )


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class ComplexSerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer()
    constructor = UserDataSerializer()
    """
    Serializer for Complex model
    """

    class Meta:
        model = Complex
        fields = (
            "id",
            "name",
            "description",
            "amenities",
            "date_built",
            "constructor",
            "website",
            "images",
        )


class BuildingSerializer(serializers.ModelSerializer):
    """
    Serializer for Building model
    """

    complex = ComplexSerializer()
    address = AddressSerializer()

    class Meta:
        model = Building
        fields = (
            "name",
            "floors",
            "complex",
            "address",
        )

    def get_address(self, obj):
        serializer = AddressSerializer(obj.address)
        return serializer.data


class ContractSerializer(serializers.ModelSerializer):
    """
    Serializer for Contract model
    """

    class Meta:
        model = Contract
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for Property model
    """

    amenities = AmenitySerializer(many=True)
    building = BuildingSerializer()
    owner = UserDataSerializer()

    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "building",
            "property_type",
            "owner",
            "price",
            "availability",
            "floor",
            "rooms",
            "bathrooms",
            "area",
            "amenities",
            "description",
            "images",
        )
