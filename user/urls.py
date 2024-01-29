from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='home'),
    path('add_user/', views.add_user, name='add-user'),
    path('view_users/', views.view_users, name='view_user'),
    path('update_user/<int:pk>/', views.update_user, name='update-user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete-user'),
]
