from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassesListView
from .views import ClassPeriodListView
from .views import StudentDetailView

urlpatterns = [
    path("students/" ,StudentListView.as_view(),name="student_list_view"),
    path("teachers/" ,TeacherListView.as_view(),name="teacher_list_view"),
    path("courses/" ,CourseListView.as_view(),name="course_list_view"),
    path("classes/" ,ClassesListView.as_view(),name="classes_list_view"),
    path("class_periods/" ,ClassPeriodListView.as_view(),name="class_periods_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),

]