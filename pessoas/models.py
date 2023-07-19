from django.db import models

class Pessoa (models.Model):
    nome = models.CharField(("Nome"), max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nome}"