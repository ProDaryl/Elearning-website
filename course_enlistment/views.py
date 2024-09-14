from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Module, Content, UserProgress
from django.contrib.auth.decorators import login_required
from course_enrollment import  models
from django.contrib import messages

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_enlistment/course_list.html', {'courses': courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = course.modules.all()
    enrolled = models.Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'course_enlistment/course_detail.html', {'course': course, 'modules': modules, 'enrolled': enrolled})

# @login_required
# def enroll_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     enrollment, created = models.Enrollment.objects.get_or_create(user=request.user, course=course)
#     if created:
#         messages.success(request, f'You have successfully enrolled in {course.title}')
#     else:
#         messages.info(request, f'You are already enrolled in {course.title}')
#     return redirect('course_detail', course_id=course.id)

@login_required
def track_progress(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    progress, created = UserProgress.objects.get_or_create(user=request.user, content=content)
    if request.method == 'POST':
        progress.completed = True
        progress.save()
        messages.success(request, 'Progress updated successfully!')
    return render(request, 'course_enlistment/progress.html', {'content': content, 'progress': progress})

@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    contents = module.contents.all()
    return render(request, 'course_enlistment/module_detail.html', {'module': module, 'contents': contents})

@login_required
def track_module_progress(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    contents = module.contents.all()
    completed_contents = UserProgress.objects.filter(user=request.user, content__in=contents, completed=True).count()
    total_contents = contents.count()
    progress_percentage = (completed_contents / total_contents) * 100 if total_contents > 0 else 0
    return render(request, 'course_enlistment/module_progress.html', {'module': module, 'progress_percentage': progress_percentage})


# from django.shortcuts import render
# from .models import Course

# def search_courses(request):
#     query = request.GET.get('q', '').strip()
#     if query:
#         results = Course.objects.filter(title__icontains=query)
#     else:
#         results = Course.objects.all()
#     return render(request, 'course_enlistment/search_results.html', {'courses': results})

