from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'), #camonho para home
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('empresas/nova/', views.criar_empresa, name='criar_empresa'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo/', views.criar_funcionario, name='criar_funcionario'),
]
