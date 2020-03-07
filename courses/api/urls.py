from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    # list subjects
    path('subjects/', views.SubjectListAPIView.as_view(), name='subject_list'),

    # subject detail
    path('subjects/<pk>/', views.SubjectDetailAPIView.as_view(),
        name='subject_detail'),
]
