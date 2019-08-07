from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Turma(models.Model):
	cod_turma = models.AutoField(primary_key=True)
	semestre = models.CharField(max_length=30)
	
	def __str__(self):
		return self.semestre

class Aluno(models.Model):
	matricula = models.AutoField(primary_key=True)
	semestre = models.ForeignKey(Turma, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100)
	data_nac = models.CharField(max_length=12, null=True)
	user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.nome)

class Diciplina(models.Model):
	cod_diciplina = models.AutoField(primary_key=True)
	nome_diciplina = models.CharField(max_length=30)
	nota_aprovacao = models.DecimalField(max_digits=4, decimal_places=2)
	semestre_aberto = models.BooleanField(default=False)
	def __str__(self):
		return self.nome_diciplina


class Aluno_Diciplina(models.Model):
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	diciplina = models.ForeignKey(Diciplina, on_delete=models.CASCADE)
	n1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=0)
	n2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=0)
	n3 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=0)
	media = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, default=0)
	situacao = models.CharField(max_length=50, blank=True)
	faltas = models.IntegerField(null=True, default=0)

	def __str__(self):
		return str(self.aluno)

	def calcular_media(self):
		self.media = (self.n1 + self.n2 + self.n3)/3
		self.save()

	def definir_situacao(self, diciplina):
		diciplina = Diciplina.objects.get(nome_diciplina=diciplina)
		if diciplina.semestre_aberto == True:
			self.situacao = 'Cursando'
		else:
			if self.media >= 7:
				self.situacao = 'Aprovado'
			elif self.media >= 3 and self.media < 7:
				self.situacao = 'Recuperação'
			else:
				self.situacao = 'Reprovado'

		self.save()
	def renovar(self):
		self.n1 = 0
		self.n2 = 0
		self.n3 = 0
		self.media = 0
		self.faltas = 0
		self.save()
class Professor(models.Model):
	user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

	diciplinas = models.ManyToManyField(Diciplina)

	def __str__(self):
		return str(self.user)
