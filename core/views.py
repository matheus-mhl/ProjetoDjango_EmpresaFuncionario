from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa, Funcionario
from .forms import EmpresaForm, FuncionarioForm


# Empresas

def home(request):
    return render(request, "core/base.html")

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'core/empresa_list.html', {'empresas': empresas})

def criar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')  # sem namespace por segurança
    else:
        form = EmpresaForm()
    return render(request, 'core/empresa_form.html', {'form': form})

# Funcionários
def lista_funcionarios(request):
    funcionarios = Funcionario.objects.select_related('empresa').all()
    return render(request, 'core/funcionario_list.html', {'funcionarios': funcionarios})

def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')  # sem namespace
    else:
        form = FuncionarioForm()
    return render(request, 'core/funcionario_form.html', {'form': form})
