from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.Home, name="Home" ),
    path('room/<str:id>', view=views.Room_View, name="Room"),
    path('create_room', view=views.create_room, name="Create_Room"),
    path('add_room', view=views.add_room, name="AddRoom"),
    path('update_room/<str:id>', view=views.update_room, name="Update_Room"),
    path('delete_room/<str:id>', view=views.delete_room, name="Delete_Room"),
    path('edit_room/<str:id>', view=views.edit_room, name="UpdateRoom"),
    path('remove_room/<str:id>', view=views.remove_room, name="DeleteRoom")
]
  