from django.db import models

class MiModelo(models.Model):
    mi_campo = models.CharField(max_length=100)
