from django.contrib import admin
from galeria.models import Fotografia, Pessoa

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

class ListandoPessoa(admin.ModelAdmin):
    list_display = ("cpf","nome","telefone")
    list_display_links = ("cpf","nome")
    search_fields = ("nome",)
    list_filter = ("nome",)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Pessoa, ListandoPessoa)
