from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room
from course_enlistment import models


# Create your views here.
@login_required
def home(request):
    rooms = Room.objects.all()
    return render(request, 'chatroom/chat.html', {'rooms': rooms})

@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chatroom/group.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

@login_required
def checkview(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room_name).exists():
            return redirect(f'room/{room_name}/?username={username}')
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect(f'room/{room_name}/?username={username}')
    else:
        # Handle the case where the method is not POST
        return redirect('chat_index')  # Redirect or handle accordingly

@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required
def getMessages(request, room):
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        raise Http404("Room not found")

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})