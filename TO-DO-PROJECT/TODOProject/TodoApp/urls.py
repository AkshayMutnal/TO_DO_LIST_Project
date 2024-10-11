
from django.urls import path
from . import views

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('profile/', views.user_profile, name='user_profile'), 
    path('register/', views.register, name='register'),  
    path('', views.login_view, name='login'),      
    path('logout/', views.logout_view, name='logout'), 
]
