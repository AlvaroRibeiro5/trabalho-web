from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia, Pessoa
from django.shortcuts import redirect
 
def index(request):
    categoria_selecionada = request.GET.get('categoria', None)
    categorias_disponiveis = [opcao[0] for opcao in Fotografia.OPCOES_CATEGORIA]
    if categoria_selecionada and categoria_selecionada in categorias_disponiveis:
        fotografias = Fotografia.objects.filter(categoria=categoria_selecionada, publicada=True).order_by("-data_fotografia")
    else:
        fotografias = Fotografia.objects.filter(publicada=True).order_by("-data_fotografia")

    return render(request, 'galeria/index.html', {"cards": fotografias, "categorias": categorias_disponiveis})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})

def sucesso(request):
    return render(request, 'galeria/sucesso.html')

def contato(request):
    return render(request, 'galeria/contato.html')

def form(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        endereco = request.POST['endereco']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha = request.POST['senha']

        pessoa = Pessoa(
            cpf=cpf,
            nome=nome,
            data_nascimento=data_nascimento,
            endereco=endereco,
            telefone=telefone,
            email=email,
            senha=senha
        )
        pessoa.save()

        return redirect('sucesso')  # Redirecione para a página de sucesso
    return render(request, 'galeria/form.html')

def casa_do_leo(request):
    return render(request, 'galeria/casa_do_leo.html')

def contribuir(request):
    return render(request, 'galeria/contribuir.html')
