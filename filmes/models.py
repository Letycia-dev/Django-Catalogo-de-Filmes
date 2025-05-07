from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    capa = models.ImageField(upload_to='capas/')

    def __str__(self):
        return self.titulo
