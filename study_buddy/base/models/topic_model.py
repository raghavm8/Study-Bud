from django.db import models
import uuid

class Topic(models.Model):
    name = models.CharField(max_length=200)
    topic_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    def __str__(self):
        return self.name