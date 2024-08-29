from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
    # path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.log_out, name='logout'),
    path('course/', views.course, name='course'), 
    # path('teacher/', views.teacher, name='teacher'),
    path('profile', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('select_role', views.select_role, name='select_role'),
    path('forms', views.role_form, name='forms')
]