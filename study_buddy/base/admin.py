from django.contrib import admin
from .models.room_model import Room
from .models.message_model import Message
from .models.topic_model import Topic

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)