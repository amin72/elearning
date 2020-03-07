from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


app_name = 'students'

urlpatterns = [
    # register student
    path('register/', views.StudentRegistrationView.as_view(),
        name='student_registration'),

    # enroll course
    path('enroll-course/', views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),

    # list student courses
    path('courses/', views.StudentCourseListView.as_view(),
        name='student_course_list'),

    # student course detail
    path('course/<pk>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),

    # student course detail with module
    path('course/<pk>/<module_id>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'),
]
