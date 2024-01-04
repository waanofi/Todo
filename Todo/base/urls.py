from django.urls import path
from . import views

# from .views import EmployeeCreate

urlpatterns = [
   
    path("", views.index, name="index"),
    path('show', views.show, name='show'),
    path('delete<int:id>/', views.remove, name='delete'),
]

