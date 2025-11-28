from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField("CNPJ", max_length=20, blank=True)
    endereco = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"

class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='funcionarios')
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()
    email = models.EmailField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} — {self.cargo}"
