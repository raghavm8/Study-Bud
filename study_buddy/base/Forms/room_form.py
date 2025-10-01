from django.forms import ModelForm
from ..models.room_model import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        