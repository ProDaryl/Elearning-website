<<<<<<< HEAD
from django.urls import include, path
=======
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
>>>>>>> 1631a8e1a0468c37b92b59c1a6f3b4158cb451ba
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
<<<<<<< HEAD
    path('dashboard', views.dashboard, name='dashboard'),
    path('course/', views.course, name='course'), 
    path('teacher/', views.teacher, name='teacher'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('select_role', views.select_role, name='select_role'),
    path('forms', views.role_form, name='forms')
]
=======
    # path('dashboard', views.dashboard, name='dashboard'),
    path('forms', views.role_form, name='forms'),
    path('logout', views.log_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 1631a8e1a0468c37b92b59c1a6f3b4158cb451ba
