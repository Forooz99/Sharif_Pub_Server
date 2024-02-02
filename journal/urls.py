from django.urls import path
from journal.views import *

urlpatterns = [
    path('', JournalsAPI.as_view()),
    path('<slug:pk>/', JournalByIdAPI.as_view()),
    path('volumes/', VolumesAPI.as_view()),
    path('volumes/<slug:pk>/', VolumeByIdAPI.as_view()),
]
