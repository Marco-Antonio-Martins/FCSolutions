from django.contrib import admin
from .models import Pessoa, Post, Comentario

admin.site.register(Pessoa)
admin.site.register(Comentario)
admin.site.register(Post)