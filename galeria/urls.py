from django.urls import path
from galeria.views import index, imagem, form, casa_do_leo, contribuir, sucesso, contato

urlpatterns = [
    path('',index, name='index'),
    path('imagem/<int:foto_id>',imagem, name='imagem'),
    path('form/',form, name='form'),
    path('casa_do_leo/',casa_do_leo, name='casa_do_leo'),
    path('contribuir/',contribuir, name='contribuir'),
    path('sucesso/',sucesso, name='sucesso'),
    path('contato/',contato, name='contato'),
]