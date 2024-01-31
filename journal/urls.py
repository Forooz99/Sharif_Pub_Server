from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_journals, name="view_journals"),
    path('add_journal/', views.add_journal, name="add_journal"),
    path('update_journal/<int:pk>/', views.update_journal, name="update_journal"),
    path('delete_journal/<int:pk>/', views.delete_journal, name="delete_journal"),
    path('add_volume/', views.add_volume, name="add_volume"),
    path('view_volumes/', views.view_volumes, name="view_volumes"),
    path('update_volume/<int:pk>/', views.update_volume, name="update_volume"),
    path('delete_volume/<int:pk>/', views.delete_volume, name="update_volume"),
]