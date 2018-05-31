from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField('email', max_length=150)
    telefone = models.CharField('email', max_length=50)
    '''data_inicio = models.DateField()
    data_fim = models.DateField()'''

    def __str__(self):
        return self.nome

class Autor(Usuario):
    cpf = models.CharField('CPF', max_length=50)
    escolaridade = models.CharField('Escolaridade', max_length=150)
    descricao = models.TextField()

    def __str__(self):
        return self.cpf

class Categoria(models.Model):
    titulo = models.CharField('titulo', max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField('titulo', max_length=250)
    subtitulo = models.CharField('subtitulo', max_length=550)
    descricao = models.TextField('', max_length=550)
    data_inicio = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



