from django.db import models
from datetime import datetime
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("Zona Norte", "ZONA NORTE"),
        ("Zona Sul", "ZONA SUL"),
        ("Zona Leste", "ZONA LESTE"),
        ("Zona Oeste", "ZONA OESTE"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now,blank=False)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    cpf = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome