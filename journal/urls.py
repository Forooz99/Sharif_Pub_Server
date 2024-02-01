from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_journals, name="view_journals"),  # get all journals GET
    path('get/<slug:pk>/', views.get_journal, name="get_journal"),  # get a specific journal GET
    path('add/', views.add_journal, name="add_journal"),  # add new journal POST
    path('update/<slug:pk>', views.update_journal, name="update_journal"),  # update a journal PUT
    path('delete/<slug:pk>', views.delete_journal, name="delete_journal"),  # delete a journal DELETE
    path('volumes/', views.view_volumes, name="view_volumes"),  # get all volumes GET
    path('volumes/get/<int:pk>/', views.get_volume, name="get_volume"),  # get a specific volume GET
    path('volumes/add/', views.add_volume, name="add_volume"),  # add new volume POST
    path('volumes/update/<int:pk>/', views.update_volume, name="update_volume"),  # update a volume PUT
    path('volumes/delete/<int:pk>/', views.delete_volume, name="delete_volume"),  # delete a volume DELETE
]