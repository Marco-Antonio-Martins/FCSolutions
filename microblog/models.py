from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário', unique=True)
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome

    def arroba(self):
        return self.usuario.get_username()

class Post(models.Model):

    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Autor")
    conteudo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-data",)
    
    '''def __str__(self):
        return self.conteudo[:20]''' #Ta apagando e não só pra visualização
    
    def __str__(self):
        return self.conteudo

class Comentario(models.Model):
    
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Autor")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    conteudo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("data",)

        