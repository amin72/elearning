from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'courses'


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)


urlpatterns = [
    # list subjects
    path('subjects/', views.SubjectListAPIView.as_view(), name='subject_list'),

    # subject detail
    path('subjects/<pk>/', views.SubjectDetailAPIView.as_view(),
        name='subject_detail'),

    # enroll in a course
    path('courses/<pk>/enroll/', views.CourseEnrollAPIView.as_view(),
        name='course_enroll'),

    path('', include(router.urls)),
]
