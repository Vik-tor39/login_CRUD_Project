from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ContentListView.as_view(), name='contenidos'),
    path('add/', ContentCreateView.as_view(), name='create'),
    path('detail/<int:pk>/<slug:content_slug>', ContentDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/<slug:content_slug>',  ContentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/',  ContentDeleteView.as_view(), name='delete'),
]