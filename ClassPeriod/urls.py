from django.urls import path
from . import views

urlpatterns = [
    path('class-periods/', views.ClassPeriodListView.as_view(), name='class-period-list'),
]