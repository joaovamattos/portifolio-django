from django.db import models
from django.contrib import admin

class Post(models.Model):
    titulo = models.CharField(max_length = 255)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    texto = models.TextField()
    foto = models.ImageField()

admin.site.register(Post)

     
