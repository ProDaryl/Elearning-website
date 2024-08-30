from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat_index'),
    # path('group', views.checkview, name='group'),
    # path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('room/<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
]
