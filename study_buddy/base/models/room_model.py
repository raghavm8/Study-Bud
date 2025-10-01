from django.db import models
import uuid
from django.contrib.auth.models import User
from .topic_model import Topic

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    
    class Meta: 
        ordering = ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.name
    