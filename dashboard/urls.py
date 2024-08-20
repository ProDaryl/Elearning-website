from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_board, name='dashboard'),
    path('notes', views.notes, name='notes'),
    path('delete_notes/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),
    path('homework',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('youtube',views.youtube,name="youtube"),
]