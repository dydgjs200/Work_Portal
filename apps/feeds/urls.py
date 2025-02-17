from django.urls import path
from .views import add_Feed

urlpatterns = [
    path('addfeed/', add_Feed, name = "add_Feed")
]