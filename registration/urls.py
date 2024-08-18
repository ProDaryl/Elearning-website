from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('select_role', views.select_role, name='select_role'),
    path('forms', views.role_form, name='forms')
]