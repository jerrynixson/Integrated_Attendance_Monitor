from django.urls import path
from . import views
from .api_views import api_mark_attendance, list_students_by_class

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('view/', views.view_attendance, name='view_attendance'),
    path('api/mark/', api_mark_attendance, name='api_mark_attendance'),
    path('api/class/<int:class_id>/students/', list_students_by_class, name='list_students_by_class'),
    path('api/class/<int:class_id>/records/', views.get_class_records, name='get_class_records'),  # Add this line
]
