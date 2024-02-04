from django.urls import path
from journal.views import *

urlpatterns = [
    path('volumes', VolumesAPI.as_view()),
    path('volumes/<str:pk>', VolumeByIdAPI.as_view()),
    path('<slug:pk>', JournalByIdAPI.as_view()),
    path('', JournalsAPI.as_view()),
]
