from django.urls import path
from . import views
from .views import TaskList,  TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', views.dash_board, name='dashboard'),
    path('notes', views.notes, name='notes'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task/create', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('delete_notes/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),
    path('homework', views.homework, name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('youtube', views.youtube, name="youtube"),
    path('dictionary', views.dictionary, name='dictionary'),
    path('word', views.word, name='word'),
]