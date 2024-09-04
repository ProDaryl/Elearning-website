from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('chat/', include('chatroom.urls')),
    path('courses/', include('course_enlistment.urls')),
    path('api/', include('course_enrollment.urls')),
]
