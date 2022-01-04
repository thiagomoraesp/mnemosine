from django.db import models

class Pais(models.Model):
    codigo = models.CharField("Código do país(E.g: BR)",max_length=3)
    nome = models.CharField(max_length=200)    

class Estado(models.Model):
    sigla = models.CharField("Sigla",max_length=3)
    nome = models.CharField(max_length=200)
    pais_id = models.ForeignKey(Pais, on_delete=models.PROTECT)

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    estado_id = models.ForeignKey(Estado, on_delete=models.PROTECT)

class Conteudo(models.Model):
    imagem = models.CharField("Imagem",null=True,max_length=1000)
    link = models.CharField("Link",null=True,max_length=1000)
    descricao=models.TextField("Descrição")
    data_aproximada = models.DateField("Data Aproximada")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    CEP = models.CharField("CEP",max_length=11,null=True)
    autor = models.CharField("Autor(deixo em branco caso autor seja desconhecido)",max_length=200,null=True)

class Report(models.Model):
    conteudo_id = models.ForeignKey(Conteudo,on_delete=models.PROTECT)
    descricao = models.TextField("Descrição")
    data_hora = models.DateTimeField("Data/hora")
    contato = models.CharField("Email/Telefone",max_length=300)
    