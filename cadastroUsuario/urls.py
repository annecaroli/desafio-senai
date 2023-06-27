from django.urls import path
from cadastroUsuario.views import index

urlpatterns = [
    path('', index)
]
