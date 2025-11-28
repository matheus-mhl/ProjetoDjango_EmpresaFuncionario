from django.contrib import admin
from .models import Empresa, Funcionario

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email', 'telefone', 'criado_em')
    search_fields = ('nome', 'cnpj')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'empresa', 'salario', 'ativo')
    list_filter = ('empresa', 'cargo', 'ativo')
    search_fields = ('nome', 'cargo', 'empresa__nome')
