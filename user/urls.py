from django.urls import path

from user.views import *

urlpatterns = [
    path('', views.UserOverview, name='user'),
    path('signup/', ReaderView.as_view(), name='add-user'),
    path('login/', views.add_user, name='add-user'),
    path('all/', views.view_user, name='view_user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete-user'),
]
