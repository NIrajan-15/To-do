from django.urls import path
from . import views
from .views import TaskView

urlpatterns = [
    
    path('', views.main, name="list"),
    path('upadates_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('home', TaskView.as_view() ),
]