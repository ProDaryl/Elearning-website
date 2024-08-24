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
    path('forms', views.role_form, name='forms'),
    path('logout', views.log_out, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
