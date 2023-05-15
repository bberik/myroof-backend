from django.urls import path
from . import views
from .views import (
    PropertyListView,
    BuildingListView,
    PropertyDetailView,
    RegisterView,
    MyTokenObtainPairView
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", PropertyListView.as_view()),
    path("create", views.PostPropertyView),
    path("property/<pk>", PropertyDetailView.as_view()),
    path('register', RegisterView.as_view(), name="sign_up"),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('my-properties', views.ListedPropertiesView),
    path('update-profile', views.UpdateProfileView),
    path('buildings', BuildingListView.as_view()),
]

