from django.urls import path
from cadastroUsuario.views import index, cadastro, editar

urlpatterns = [
    path('', index),
    path('cadastro', cadastro, name='cadastro'),
    path('editar', editar),
]
