from django.shortcuts import render
from chats.models import Course,message

# Create your views here.
def room(request):
    return render(request, 'room.html')
def course(request, Course):
    return render(request='chats.html')
def checkview(request):
    course = request.POST['course_name']
    username = request.POST['username']

    if Course.objects.filter(name = course).exists():
        return redirect('/'+course+'/username'+username)
    else:
        new_course = course.objects.Create(name=course)
        new_course.saver()
        return redirect('/'+course+"/?username="+username)