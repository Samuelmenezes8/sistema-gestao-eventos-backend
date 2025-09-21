from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'local', 'capacidade')
    list_filter = ('data', 'local')
    search_fields = ('titulo', 'descricao')