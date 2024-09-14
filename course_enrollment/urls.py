from django.urls import path
from .views import *

urlpatterns = [
    path('enroll/<int:course_id>', EnrollView.as_view(), name='enroll'),
    path('uneroll/', UnenrollView.as_view(), name='unenroll'),
    path('enrollments/', EnrollmentListView.as_view() , name='enrollments-list'),
]
