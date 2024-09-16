from django.shortcuts import redirect, render

from course_enlistment.models import Course
from course_enrollment.models import Enrollment
from  .forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
from PyDictionary import PyDictionary
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

# @login_required 
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = context['tasks'].filter(user=self.request.user)
    #     context['count'] = context['tasks'].filter(complete=False).count()

    #     # search_input = self.request.GET.get('search-area') or ''
    #     # if search_input:
    #     #     context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        # return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'dashboard/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


@login_required
def dash_board(request):
    courses = Course.objects.all()
    enrolled_courses = Course.objects.filter(enrollment__user=request.user)
    return render(request, 'dashboard/home.html', {'courses': enrolled_courses})

@login_required
def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user = request.user, title = request.POST['title'], description = request.POST['description'])
            notes.save()
        messages.success(request, 'Notes Added from {request.user.username} Successfully!')
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user = request.user)
    context = {'notes' : notes,'form' : form}
    return render(request, 'dashboard/notes.html', context)

@login_required
def delete_note(request, pk=None):
    Notes.objects.get(id = pk).delete()
    return redirect("notes")

class NotesDetailView(generic.DetailView):
    model = Notes


@login_required
def homework(request):
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
                
            )
            homeworks.save()
            messages.success(request, f'Homework Added from {request.user.username}!!')
    else:
         form = HomeWorkForm()

    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False

    context = {'homeworks' : homework, 
               'homework_done' : homework_done, 
               'form':form,
               }
    return render(request, 'dashboard/homework.html', context)


@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

@login_required
def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')


@login_required
def youtube(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime']
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form': form,
                'results':result_list
            }
        return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardForm()
    context = {'form':form}
    return render(request, 'dashboard/youtube.html',context)


@login_required
def dictionary(request):
    return render(request, 'dashboard/dictionary.html')

@login_required
def word(request):
    search = request.GET.get('word-search')
    dictionary = PyDictionary()

    meaning = None
    synonyms = None
    antonyms = None

    try:
        # Fetch the meaning, synonyms, and antonyms from the dictionary
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)
    except Exception as e:
        print(f"Error fetching dictionary data: {e}")

    # Prepare context with fallback values if any data is missing
    context = {
        'meaning': meaning['Noun'][0] if meaning and 'Noun' in meaning else "No meaning found",
        'synonyms': synonyms if synonyms else ["No synonyms found"],
        'antonyms': antonyms if antonyms else ["No antonyms found"],
    }

    return render(request, 'dashboard/word.html', context)