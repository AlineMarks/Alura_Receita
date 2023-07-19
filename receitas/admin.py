from django.contrib import admin
from .models import Receitas

class ListandoReceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 2
    
admin.site.register(Receitas,ListandoReceita)