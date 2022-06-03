from django.http import Http404
from django.shortcuts import render
from .models import Pessoa

def perfil(request, user):

    try:
        pessoa = Pessoa.objects.get(usuario__username__contains=user)

    except Pessoa.DoesNotExist:

        raise Http404('Nome de Usuário não encontrado')

    return render(request, 'microblog/index.html', {'pessoa' : pessoa})


    

    
    
