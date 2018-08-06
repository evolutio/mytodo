from django.contrib import admin

# Register your models here.
from core.models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'feita', 'created')


admin.site.register(Tarefa, TarefaAdmin)
