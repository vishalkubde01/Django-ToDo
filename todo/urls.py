from django.urls import path
from . import views

urlpatterns = [
  # add task 
  path('addTask/', views.addTask, name='addTask'),

  # mark_as_done 
  path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
  
  # mark_as_not_done
  path('mark_as_not_done/<int:pk>/', views.mark_as_not_done, name='mark_as_not_done'),

  # Edit task feature
  path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

  # Delete task feature
  path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
