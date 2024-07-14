from django.urls import path
from .views import StudentListView
from . import views

urlpatterns =[
    path("students/", StudentListView.as_view(),name="student_list_view"),
    path('class-periods/', views.ClassPeriodListView.as_view(), name='class-period-list'),
]



