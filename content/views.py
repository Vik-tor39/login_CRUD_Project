from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Contenido

# Create your views here.
class ContentListView(ListView):
    model = Contenido