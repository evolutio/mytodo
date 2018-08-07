from core.models import Tarefa


def list_tarefas():
    tarefas = [t.to_dict_json() for t in Tarefa.objects.all()]
    return tarefas


def add_tarefa(dtarefa):
    tarefa = Tarefa.objects.create(tarefa=dtarefa['tarefa'], feita=dtarefa['feita'])
    return tarefa.to_dict_json()


def remove_tarefa(tarefa_id):
    Tarefa.objects.get(pk=tarefa_id).delete()
