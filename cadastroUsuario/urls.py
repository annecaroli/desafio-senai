from django.urls import path
from cadastroUsuario.views import index, cadastro_usuario, editar_usuario

urlpatterns = [
    path('', index),
    path('cadastro-usuario', cadastro_usuario),
    path('editar-usuario', editar_usuario),

]
