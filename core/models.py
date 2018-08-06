from django.db import models

# Create your models here.


class Tarefa(models.Model):
    tarefa = models.CharField(max_length=512)
    feita = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def to_dict_json(self):
        return {
            'id': self.id,
            'tarefa': self.tarefa,
            'feita': self.feita,
            'created': self.created,
        }
