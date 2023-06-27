from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cadastroUsuario.models import CadastroUsuario


def index(request):
    users = CadastroUsuario.objects.all()
    return render(request, 'cadastroUsuario/index.html', {"cards": users})

def usuario(request, user_id):
    user = get_object_or_404(CadastroUsuario, pk=user_id)
    return render(request, 'cadastroUsuario/user.html', {'user': user})

def cadastro_usuario(request):
    return render(request, 'cadastroUsuario/cadastro-usuario.html')

def editar_usuario(request):
    return render(request, 'cadastroUsuario/editar-usuario.html')