from django.shortcuts import render
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

# View para editar contenido
class ContentUpdateView(UpdateView):
    model = Contenido
    fields = ["title", 'content', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id, slugify(self.object.title))) + '?ok'

# View para eliminar contenido
class ContentDeleteView(DeleteView):
    model = Contenido
    success_url = reverse_lazy("contenidos")