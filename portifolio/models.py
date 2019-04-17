from django.db import models
from django.contrib import admin



class Job(models.Model):
    descricao = models.TextField()
    foto = models.ImageField()

admin.site.register(Job)