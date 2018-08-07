from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),

    url(r'^api/add_tarefa$', views.add_tarefa),
    url(r'^api/remove_tarefa$', views.remove_tarefa),
    url(r'^api/list_tarefas$', views.list_tarefas),
]