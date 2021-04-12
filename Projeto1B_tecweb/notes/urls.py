from django.urls import path

from . import views

#para melhorar o encapsulamento
# notes/urls.py vai controlar as rotas das notas

# quando a rota vazia ('') for acessada, 
# o django deve utilizar a função views.index para construir a resposta

# funções são objetos de primeira classe no python
# por isso podemos passar uma função como argumento
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('tags', views.tags_list), # lista de tags
    path('tag/<str:tag>', views.tag) # tags individuais
]