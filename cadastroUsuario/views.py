from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cadastroUsuario.models import CadastroUsuario
from cadastroUsuario.forms import CadastroForms


def index(request):
    users = CadastroUsuario.objects.all()
    return render(request, 'cadastroUsuario/index.html', {"cards": users})

def usuario(request, user_id):
    user = get_object_or_404(CadastroUsuario, pk=user_id)
    return render(request, 'cadastroUsuario/user.html', {'user': user})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form['nome'].value()
            cpf = form['cpf'].value()
            login = form['login'].value()
            senha = form['senha'].value()

            if CadastroUsuario.objects.filter(login=login).exists():
                return render(request, 'cadastroUsuario/cadastro.html')

            usuario = CadastroUsuario.objects.create(
                nome = nome,
                cpf = cpf,
                login = login,
                senha = senha
            )
            usuario.save()
            return render(request, 'cadastroUsuario/index.html')

    return render(request, 'cadastroUsuario/cadastro.html', {"form": form})

def editar(request):
    return render(request, 'cadastroUsuario/editar.html')