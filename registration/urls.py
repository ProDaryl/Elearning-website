from django.urls import path
from . import views


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('course/', views.course, name='course'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('submission-successful/', views.submission_successful_view, name='submission_successful'),
    path('select_role', views.select_role, name='select_role'),
    path('forms', views.role_form, name='forms')
]