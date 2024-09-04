from django.urls import path
from .views import *

urlpatterns = [
    path('eroll/', EnrollView.as_view(), name='enroll'),
    path('uneroll/', UnenrollView.as_view(), name='uneroll'),
    path('enrollments/', EnrollmentListView.as_view() , name='enrollments-list'),
]
