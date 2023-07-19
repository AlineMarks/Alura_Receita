from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth,messages
from receitas.models import Receitas

def cadastro (request):
    if request.method == 'POST':
        nome = request.POST  ['nome']
        email = request.POST  ['email']
        senha = request.POST  ['password']
        senha2 = request.POST  ['password2']
        
        if campo_vazio(nome):
            messages.error (request,'não pode deixar o nome em branco')
            return render (request, '../templates/global/usuario/cadastro.html')
        if campo_vazio(email):
            messages.error(request,'não pode deixar o email em branco')
            return render (request, '../templates/global/usuario/cadastro.html')
        if senha_diferente(senha,senha2):
            messages.error(request,'as senhas não são iguais')
            return render (request, '../templates/global/usuario/cadastro.html')
        if User.objects.filter(email=email).exists():
            messages.error (request,'EMAIL já cadastrado')
            return render (request, '../templates/global/usuario/cadastro.html')
        if User.objects.filter(username=nome).exists():
            messages.error (request, 'Nome de usuario já cadastrado')
            return render (request, '../templates/global/usuario/cadastro.html')
        user = User.objects.create_user(username=nome, email=email,password=senha)
        user.save()
        messages.success(request,'Cadastro realizado com sucesso')
        
        return redirect ('login')
    

    else:
        return render (request, '../templates/global/usuario/cadastro.html')

def login (request):    
    if request.method == 'POST':
        email = request.POST  ['email']
        senha = request.POST  ['senha']
        
        print (email,senha)
        if campo_vazio(senha) or campo_vazio(email):
            messages.error (request,'Email e/ou Senha não pode ser em branco')
            return render (request, '../templates/global/usuario/login.html')
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request,username=nome, password=senha)
            if user is not None:
                auth.login(request,user)
                return redirect ('dashboard')
            
        return redirect ('login')
    
    else:

        return render (request, '../templates/global/usuario/login.html')

def logout (request):
    auth.logout(request)
    return redirect('index')

def dashboard (request):
    if request.user.is_authenticated:
        id = request.user.id
        receita = Receitas.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receita':receita
        }
        return render (request, '../templates/global/usuario/dashboard.html', dados)
    else:
        return redirect('index')
    
def cria_receita(request):
        if request.method == 'POST':
            nome_receita = request.POST  ["nome_receita" ]
            ingredientes = request.POST  ["ingredientes"]
            modo_preparo = request.POST  ["modo_preparo"]
            tempo_preparo = request.POST  ["tempo_preparo" ]
            rendimento = request.POST  ["rendimento"]
            categoria = request.POST  ["categoria"]
            foto_receita = request.FILES  ["foto_receita"]

            user = get_object_or_404(User, pk=request.user.id)
            receita = Receitas.objects.create(pessoa=user, nome_receita=nome_receita, ingrediente=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
            receita.save()
            return redirect ('dashboard')
        else:
            return render (request, '../templates/global/usuario/cria_receita.html')

def campo_vazio(campo):
    return not campo.strip()

def senha_diferente(senha,senha2):
    return senha != senha2