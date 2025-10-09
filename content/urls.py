from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ContentListView.as_view(), name='contenidos')
]