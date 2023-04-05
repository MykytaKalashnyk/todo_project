from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add_task/', views.AddTask.as_view(), name='add_task'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('update_status/<int:pk>', views.UpdateStatus.as_view(), name='update_status'),
]
