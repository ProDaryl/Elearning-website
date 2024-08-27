from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Content, UserProgress
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = course.modules.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'modules': modules})

@login_required
def track_progress(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    progress, created = UserProgress.objects.get_or_create(user=request.user, content=content)
    if request.method == 'POST':
        progress.completed = True
        progress.save()
    return render(request, 'courses/progress.html', {'content': content, 'progress': progress})

