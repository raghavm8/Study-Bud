from django.shortcuts import render
from django.shortcuts import redirect
from .models.room_model import Room
from .Forms.room_form import RoomForm
from .models.topic_model import Topic


def Home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics}
    return render(request, "home.html", context)


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
