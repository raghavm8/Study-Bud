from django.db import models
import uuid
from .room_model import Room
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    def __str__(self):
        return self.body