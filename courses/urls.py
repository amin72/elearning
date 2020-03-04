from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    # list user's courses
    path('mine/', views.ManageCourseListView.as_view(),
        name='manage_course_list'),

    # create course
    path('create/', views.CourseCreateView.as_view(), name='course_create'),

    # edit course
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),

    # delete course
    path('<pk>/delete/', views.CourseDeleteView.as_view(),
        name='course_delete'),
]
