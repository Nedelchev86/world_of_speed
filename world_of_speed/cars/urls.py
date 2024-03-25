
from django.contrib import admin
from django.urls import path

from world_of_speed.cars.views import CatalogueView, CarCreateView, CarDetailsView, CarEditView, CarDeleteView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name="catalogue"),
    path('create/', CarCreateView.as_view(), name="car create"),
    path('<int:pk>/details/', CarDetailsView.as_view(), name="car details"),
    path('<int:pk>/edit/', CarEditView.as_view(), name="car edit"),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name="car delete"),
]
