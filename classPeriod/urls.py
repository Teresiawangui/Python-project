from django.urls import path
from .views import ClassPeriodListView
from . import views

urlpatterns =[
    path("classPeriod/", ClassPeriodListView.as_view(),name="class_period_list_view")
   ,
]



