from django.urls import path
from . import views

# URL patterns for the course app
urlpatterns = [
    # URL pattern for the course list view
    path('', views.course_list, name='course_list'),
    
    # URL pattern for the course detail view
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    
    # URL pattern for tracking progress
    path('track/<int:content_id>/', views.track_progress, name='track_progress'),

    path('search/', views.search_courses, name='search_courses'),
]
