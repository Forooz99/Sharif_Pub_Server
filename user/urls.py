from django.urls import path
from user.views import *
from . import views

urlpatterns = [
    path('readers', ReadersAPI.as_view()),
    path('publishers', PublishersAPI.as_view()),
    path('readers/<int:pk>', ReaderByIdAPI.as_view()),
    path('publishers/<int:pk>', PublisherByIdAPI.as_view()),
    path('signup', views.signup),
    path('login', views.login),
    path('logout', views.logout),
]


# use - instead of _ in URI, no / at the end, lowercase, no file extension included, CRUD name function not be used
# in URI
