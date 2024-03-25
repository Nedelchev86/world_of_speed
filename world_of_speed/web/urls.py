
from django.contrib import admin
from django.urls import path

from world_of_speed.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index")
]
