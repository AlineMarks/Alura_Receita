from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Receitas

def index (request):
    receita = Receitas.objects.order_by('-date_receita').filter(publicada = True)
    dados = {
        'receita':receita
    }
    return render(request,'index.html', dados)

def receita (request, receita_id):
    receita = get_object_or_404(Receitas,pk=receita_id)
    receitas_exibir = {
        'receita':receita
    }
    return render (request, 'receita.html', receitas_exibir)

def buscar (request):
    lista_receita = Receitas.objects.order_by('-date_receita').filter(publicada = True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET ['buscar']
        if nome_a_buscar:
            lista_receita = lista_receita.filter(nome_receita__icontains = nome_a_buscar)
    dados = {
        'receita' : lista_receita
    }

    return render (request,'buscar.html', dados)