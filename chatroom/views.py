from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'chatroom/chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chatroom/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room_name = request.POST.get('room_name', '')
    username = request.POST.get('username', '')

    # Check if the room exists
    if Room.objects.filter(name=room_name).exists():
        # Redirect to the existing room with the username as a query parameter
        return redirect(f'chat/{room_name}/?username={username}')
    else:
        # Create a new room if it does not exist
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        # Redirect to the newly created room with the username as a query parameter
        return redirect(f'chat/{room_name}/?username={username}')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})