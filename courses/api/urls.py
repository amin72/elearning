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

    path('', include(router.urls)),
]
