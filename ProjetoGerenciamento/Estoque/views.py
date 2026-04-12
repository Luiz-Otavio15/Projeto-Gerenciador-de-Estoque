from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum,F
from Estoque.models import *

# Create your views here.


def tela_gerenciamento(request):
    produtos = Produto.objects.all()
    
    total_produto = produtos.count()

    itens_estoque = produtos.aggregate(
        total_estoque=Sum('estoque')
    )['total_estoque'] or 0
    
    valor_total = Produto.objects.aggregate(
    total=Sum(F('preco') * F('estoque'))
    )['total'] or 0
    
    for p in produtos:

        p.total = p.preco * p.estoque

    

    return render(request, 'html/tela4.html', {
        'produto':produtos, 
        'total_produto':total_produto, 
        'itens_estoque':itens_estoque, 
        'valor_total':valor_total 
    })

def tela_adicionar(request):
    if request.method == "POST":
        nome_produto = request.POST.get('nome_produto')
        categoria = request.POST.get('categoria')
        imagem = request.POST.get('imagem')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        valor = request.POST.get('valor')

        produto = Produto.objects.create(
            nome=nome_produto,
            categoria=categoria,
            imagem=imagem,
            estoque=quantidade_estoque,
            preco=valor
        )
        return render(request, 'html/tela4.html', {'sucesso': True})
    else:
        return render(request, 'html/tela3.html')
    
def tela_editar(request:HttpRequest, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.nome = request.POST.get('nome_produto')
        produto.categoria = request.POST.get('categoria')
        produto.imagem = request.POST.get('imagem')
        produto.estoque = request.POST.get('quantidade_estoque')
        produto.preco = request.POST.get('valor')

        produto.save()
        return redirect('tela_gerenciamento')

    return render(request, 'html/tela3.html', {'produto':produto})