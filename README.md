# Sistema de Empresas e Funcionários

## Integrantes
- Matheus Horta Lago
- Michael Gouveia
- Arthur Zavoudakis

---

## Descrição do Projeto
Este projeto é um **Sistema de Gestão de Empresas e Funcionários** desenvolvido em Django.  
Ele permite o gerenciamento de empresas, cadastro de funcionários, além de fornecer uma interface administrativa para administração dos registros via Django Admin.

Principais funcionalidades:
- Cadastro de empresas.
- Cadastro de funcionários vinculados a cada empresa.
- Administração completa via portal `/admin`.

---

## Models Criados

### Empresa
    nome = models.CharField(max_length=200)
    cnpj = models.CharField("CNPJ", max_length=20, blank=True)
    endereco = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

### Funcionário
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='funcionarios')
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()
    email = models.EmailField(blank=True)
    ativo = models.BooleanField(default=True)

---

## 💻 Tecnologias Usadas
- **Python 3.11**  
- **Django 4.2**  
- **HTML + CSS**
- **SQLite (banco de dados padrão do Django)**  

---

## ⚙️ Instruções para Rodar

1. **Clonar o projeto** ou copiar a pasta para seu computador.  
2. **Criar e ativar ambiente virtual** (opcional, mas recomendado):
3. **Instalar dependências**: pip install -r requirements.txt
4. **Rodar migrações**: python manage.py migrate 
5. **Criar superusuário (para acessar o admin)**: python manage.py createsuperuser
6. **Rodar o servidor**: python manage.py runserver
7. **Acessar a página inicial**: http://127.0.0.1:8000/
8. **Acessar o portal Admin**: http://127.0.0.1:8000/admin
9. **Usuario e Senha**: Para acessar o ambiente virtual desenvovlido utilize--> Usuário: admin1234 | Senha: admin
