from django.urls import path
from .views import add_feed, edit_feed, delete_feed

urlpatterns = [
    path('addfeed/', add_feed, name = "add_feed"),
    path('editfeed/', edit_feed, name = "edit_feed"),
    path('deletefeed/', delete_feed, name = "delete_feed")
]