from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('delete_account/<int:pk>', views.delete_account, name='delete_account'),
    path('all_readers', views.all_readers, name='all_readers'),
    path('all_publishers', views.all_publishers, name='all_publishers'),
]
