from django.urls import include, path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', login_view, name='login'),
]