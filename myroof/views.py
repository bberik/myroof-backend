import json


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
)

from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegisterSerializer, PropertySerializer, UserDataSerializer, BuildingSerializer
from .models import Property, Building, Amenity

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['mobile'] = user.mobile
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class BuildingListView(ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class PropertyDetailView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostPropertyView(request):
    user = request.user
    data = request.data
    amenities_list = data.pop('amenities', [])
    building_name = data.pop('building')
    city_name = data.pop('city')
    complex_name = data.pop('complex')

    # Retrieve building, city, and complex objects from database
    try:
        building = Building.objects.get(name=building_name, address__city=city_name, complex__name=complex_name)
    
    except (Building.DoesNotExist):
        return Response({'error': 'Invalid building.'}, status=status.HTTP_400_BAD_REQUEST)

    new_property = Property(owner=user, building=building, **data)
    new_property.save()

    amenities = []
    for name in amenities_list:
        try:
            amenity = Amenity.objects.get(name=name.strip())
        except Amenity.DoesNotExist:
            # Create a new Amenity object and save it to the database
            amenity = Amenity(name=name.strip())
            amenity.save()

        new_property.amenities.add(amenity)

    # Create and save new Property object
    # Serialize and return the new Property object
    serializer = PropertySerializer(new_property)
    return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ListedPropertiesView(request):
    user = request.user
    properties = Property.objects.filter(owner=user)
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateProfileView(request):
    user = request.user
    data = json.loads(request.body.decode('utf-8'))
    filtered_data = {k: v for k, v in data.items() if v}
    
    try:
        if 'current_password' in filtered_data and 'new_password' in filtered_data:
            current_password = filtered_data['current_password']
            new_password = filtered_data['new_password']
            if user.check_password(current_password):
                user.set_password(new_password)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError as error:
        return JsonResponse({'detail': str(error)}, status=400)
    
    try:
        user_serializer = UserDataSerializer(user, data=filtered_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=200)
        else:
            return JsonResponse(user_serializer.errors, status=400)
    except ValidationError as e:
        return JsonResponse({'detail': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'detail': str(e)}, status=500)
    

