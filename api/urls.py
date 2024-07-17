from django.urls import path
from .views import StudentListView
from .views import TeacherListView
from .views import CourseListView
from .views import ClassListView
from .views import ClassPeriodListView

urlpatterns = [
    path("students/" ,StudentListView.as_view(),name="student_list_view"),
    path("teachers/" ,TeacherListView.as_view(),name="teacher_list_view"),
    path("courses/" ,CourseListView.as_view(),name="course_list_view"),
    path("class/" ,ClassListView.as_view(),name="class_list_view"),
    path("classperiod/" ,ClassPeriodListView.as_view(),name="classperiod_list_view"),

]