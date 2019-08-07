from django.forms import ModelForm
from .models import Aluno, Turma, Diciplina, Aluno_Diciplina

class FormAluno(ModelForm):
    class Meta:
    	model = Aluno
    	fields = '__all__'

class FormAluno_Diciplina(ModelForm):
	class Meta:
		model = Aluno_Diciplina
		fields = '__all__'