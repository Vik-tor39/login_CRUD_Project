from django.shortcuts import render
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Contenido

# Mixin Class para verificar user loged:
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

# View para lista de contenido
class ContentListView(ListView):
    model = Contenido
    paginate_by = 2

# View para crear nuevo contenido 
@method_decorator(staff_member_required, name = 'dispatch')
class ContentCreateView(CreateView):
    model = Contenido
    fields = ["title", 'content', 'image']
    success_url = reverse_lazy('contenidos')

# View para visualizar contenido en detalle
class ContentDetailView(DetailView):
    model = Contenido

# View para editar contenido
@method_decorator(staff_member_required, name = 'dispatch')
class ContentUpdateView(UpdateView):
    model = Contenido
    fields = ["title", 'content', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id, slugify(self.object.title))) + '?ok'

# View para eliminar contenido
@method_decorator(staff_member_required, name = 'dispatch')
class ContentDeleteView(DeleteView):
    model = Contenido
    success_url = reverse_lazy("contenidos")