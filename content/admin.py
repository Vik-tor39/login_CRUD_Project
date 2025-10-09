from django.contrib import admin
from .models import Contenido

# Model extend configuration
class ContenidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
# Register your models here.
admin.site.register(Contenido, ContenidoAdmin)