from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('chat/', include('chatroom.urls')),
    path('courses/', include('course_enlistment.urls')),
    path('api/', include('course_enrollment.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
