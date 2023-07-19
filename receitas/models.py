from django.db import models
from datetime import datetime
from pessoas.models import Pessoa
from django.contrib.auth.models import User

class Receitas(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(("Nome da Receita"), max_length=100)
    ingrediente = models.TextField(("Ingredientes"))
    modo_preparo = models.TextField(("Modo de Preparo"))
    tempo_preparo =models.IntegerField(("Tempo de Preparo"))
    rendimento = models.CharField(("Rendimento"), max_length=100)
    categoria =  models.CharField(("Categoria"), max_length=100)
    date_receita = models.DateTimeField(("Data da Receita"), default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    publicada = models.BooleanField(default=False)

    def __str__(self): 
        return f'{self.nome_receita}'                   
                                        