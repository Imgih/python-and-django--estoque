from django.db import models

class Estoque(models.Model):
    produto_id = models.IntegerField()
    quantidade = models.IntegerField()
