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

    # update modules of given course
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
        name='course_module_update'),

    # create module content
    path('module/<int:module_id>/content/<model_name>/create/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_create'),

    # update module content
    path('module/<int:module_id>/content/<model_name>/<id>/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_update'),

    # delete module content
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(),
        name='module_content_delete'),

    # list module contents
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(),
        name='module_content_list'),

    # order modules
    path('module/order/', views.ModuleOrderView.as_view(),
        name='module_order'),

    # order contents
    path('content/order/', views.ContentOrderView.as_view(),
        name='content_order'),

    # filter courses by subject
    path('subject/<slug:subject>/', views.CourseListView.as_view(),
        name='course_list_subject'),

    # course detail
    path('<slug:slug>/', views.CourseDetailView.as_view(),
        name='course_detail'),
]
