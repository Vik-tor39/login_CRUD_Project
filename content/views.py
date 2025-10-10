from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Contenido

# Create your views here.

# View para lista de contenido
class ContentListView(ListView):
    model = Contenido
    paginate_by = 2

# View para crear nuevo contenido 
class ContentCreateView(CreateView):
    model = Contenido
    fields = ["title", 'content', 'image']
    success_url = reverse_lazy('contenidos')

# View para visualizar contenido en detalle
class ContentDetailView(DetailView):
    model = Contenido