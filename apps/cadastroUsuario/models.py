from django.db import models

class CadastroUsuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    login = models.CharField(max_length=15, null=False, blank=False)
    senha = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome
