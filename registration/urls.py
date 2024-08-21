from django.urls import include, path
from . import views


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('course/', views.course, name='course'), 
    path('teacher/', views.teacher, name='teacher'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]