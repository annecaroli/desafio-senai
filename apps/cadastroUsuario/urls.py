from django.urls import path
from apps.cadastroUsuario.views import index, cadastrar, editar, excluir

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('editar', editar, name='editar'),
    path('editar', excluir, name='excluir'),
]
