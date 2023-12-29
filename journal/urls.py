from .views import VolumeListApiView,VolumeDetailApiView, JournalListApiView, JournalDetailApiView
from django.urls import path

urlpatterns = [
    path('volume/', VolumeListApiView.as_view(),name = 'volume list view'),
    path('volume/<int:volume_id>/', VolumeDetailApiView.as_view(), name = 'volume detail view'),
    path('journal/', JournalListApiView.as_view(), name = 'journal list view'),
    path('journal/<int:journal_id>/', JournalDetailApiView.as_view(), name = 'journal detail view'),
]