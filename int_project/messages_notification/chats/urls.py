from django . urls import path
from . import views
urlpatterns =[
    path('', views.room, name='room'),
    path('<str:course>/',views.course, name='course'),
    path('checkview', views.checkview, name='checkview'),
]
