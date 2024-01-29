from django.urls import path
from . import views

urlpatterns = [
    path('journal/', views.apiOverview, name='home'),
    path('add_journal/', views.add_journal, name='add-journal'),
    path('view_journals/', views.view_journals, name='view_journals'),
    path('update_journal/<int:pk>/', views.update_journal, name='update-journal'),
    path('journal/<int:pk>/delete/', views.delete_journal, name='delete-journal'),
    path('add_volume/', views.add_volume, name='add-volume'),
    path('view_volumes/', views.view_volumes, name='view_volumes'),
    path('update_volume/<int:pk>/', views.update_volume, name='update-volume'),
    path('volume/<int:pk>/delete/', views.delete_volume, name='delete-volume'),
]