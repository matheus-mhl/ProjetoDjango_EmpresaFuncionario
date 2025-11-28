from django import forms
from .models import Empresa, Funcionario

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'endereco', 'email', 'telefone']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['empresa', 'nome', 'cargo', 'salario', 'data_admissao', 'email', 'ativo']
