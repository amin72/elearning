from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView


urlpatterns = [
    # login user
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    # logout user
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),

    path('course/', include('courses.urls')),

    # list courses
    path('', CourseListView.as_view(), name='course_list'),
]
