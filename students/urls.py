from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    # register student
    path('register/', views.StudentRegistrationView.as_view(),
        name='student_registration'),

    # enroll course
    path('enroll-course/', views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),
]
