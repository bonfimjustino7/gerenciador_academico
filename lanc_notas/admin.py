from django.contrib import admin
from .models import Turma, Aluno, Diciplina, Aluno_Diciplina, Professor
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
	list_display = ('matricula', 'nome', 'semestre','data_nac', 'user')
	#list_display = ('cod_diciplina', 'cod_turma')
class Aluno_DiciplinaAdmin(admin.ModelAdmin):
	list_display = ('aluno', 'diciplina', 'media','situacao')

class DicplinaAdmin(admin.ModelAdmin):
	list_display = ('nome_diciplina', 'nota_aprovacao', 'semestre_aberto')

class TurmaAdmin(admin.ModelAdmin):
	list_display = ('cod_turma','semestre')

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Diciplina, DicplinaAdmin)
admin.site.register(Aluno_Diciplina, Aluno_DiciplinaAdmin)