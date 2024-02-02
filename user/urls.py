from django.urls import path
from . import views


urlpatterns = [
    path('readers', views.all_readers, name='all_readers'),
    path('publishers', views.all_publishers, name='all_publishers'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>', views.delete_account, name='delete_account'),
]


# use - instead of _ in URI, no / at the end, lowercase, no file extension included, CRUD name function not be used
# in URI
