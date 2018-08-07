from django.http.response import JsonResponse
from django.shortcuts import render
from core.service import tarefa_svc
import json
from time import sleep


def index(request):
    return render(request, 'index.html', {})


def list_tarefas(request):
    tarefas = tarefa_svc.list_tarefas()
    return JsonResponse(tarefas, safe=False)


def add_tarefa(request):
    sleep(1)
    dtarefa = json.loads(request.POST['tarefa'])
    tarefa = tarefa_svc.add_tarefa(dtarefa)
    return JsonResponse(tarefa)


def remove_tarefa(request):
    sleep(1)
    tarefa_id = int(request.POST['tarefa_id'])
    tarefa_svc.remove_tarefa(tarefa_id)
    return JsonResponse({})
