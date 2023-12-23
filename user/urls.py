from django.urls import path

from user import views

urlpatterns = [
    path('', views.UserOverview, name='user'),
    path('create/', views.add_user, name='add-user'),
    path('all/', views.view_user, name='view_user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete-user'),
]
