from django.shortcuts import render
from django.shortcuts import redirect
from .models.room_model import Room
from .Forms.room_form import RoomForm
from .models.topic_model import Topic
from django.db.models import Q


def Home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__contains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "home.html", context)


def AllRooms(request):
    rooms = Room.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "room_count": room_count}
    return render(request, "all_rooms.html", context)


def AllTopics(request):
    topics = Topic.objects.all()
    context = {"topics": topics}
    return render(request, "all_topics.html", context)


def Room_View(request, id):
    room = Room.objects.get(id=id)
    context = {"room": room}
    return render(request, "room.html", context)


def create_room(request):
    form = RoomForm
    context = {"form": form}
    return render(request, "room_create_form.html", context)


def add_room(request):
    if request.method == "POST":
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("Home")

    return render(request, "home.html")


def update_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    context = {"form": form, "room": room}
    return render(request, "room_update_form.html", context)


def edit_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect("Home")

    return render(request, "home.html")


def delete_room(request, id):
    room = Room.objects.get(id=id)
    return render(request, "delete_room.html", {"obj": room})


def remove_room(request, id):
    room = Room.objects.get(id=id)
    print(room)
    if request.method == "POST":
        room.delete()
        return redirect("Home")
    return render(request, "home.html")
