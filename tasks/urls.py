from django.urls import path
from tasks.views import manager, user, taskForm, update_task, delete_task

urlpatterns = [
    path('manager', manager, name='manager'),
    path('user', user, name='user'),
    path('taskform',taskForm, name='taskForm'),
    path('update-task/<int:id>/',update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task')
]