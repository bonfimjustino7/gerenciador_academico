from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Aluno_Diciplina, Aluno, Aluno_Diciplina, Turma, Diciplina, Professor
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import FormAluno, FormAluno_Diciplina
from django.template.context import RequestContext
from django.core.exceptions import PermissionDenied
import json
# Create your views here.
def calcMedia(request, f, di):
	# alunos = Aluno_Diciplina.objects.all()
	# for aluno in alunos:
	# 	aluno.calcular_media()
	# 	aluno.definir_situacao()
	# return redirect('/alunos/aprovados')
	al = Aluno_Diciplina.objects.get(pk=f.id)
	print(dir(al))
	al.calcular_media()
	al.definir_situacao(di)

	print('Aluno passado: {} {}'.format(f.id, al))
	
	#print(dir(al))
	return redirect('/alunos/aprovados')
	
def calcular_medias(request, diciplina):
	alunos = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina = diciplina)
	for aluno in alunos:
		aluno.calcular_media()
		aluno.definir_situacao(aluno.diciplina)
	return redirect('/minhasdiciplinas')

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.view_professor', login_url='/minhasdiciplinas')
def index(request):
	aluno = Aluno.objects.all() 
	alunosAp = Aluno_Diciplina.objects.filter(situacao='Aprovado')
	alunosRec = Aluno_Diciplina.objects.filter(situacao='Recuperação')
	alunosRep = Aluno_Diciplina.objects.filter(situacao='Reprovado')

	#print(request.get_full_path())
	pagina = str(request.get_full_path())
	aux = pagina.split('/')
	print(aux)

	#prototipo
	diciplinas = Diciplina.objects
	alunos = Aluno_Diciplina.objects
	lista = [str(aluno.diciplina) for aluno in alunos.filter(situacao='Aprovado')] #pega os alunos aprovados e colola em uma lista
	lista_diciplinas = [dici.nome_diciplina for dici in diciplinas.all()] #pega todas as diciplinas
	dados = [[li, lista.count(li)] for li in lista_diciplinas]
	dados = dict(dados) #{'Calculo I': 4, 'Tecnologia Web': 5, 'Programação Orientada a Objeto': 2}

	names = [dici for dici in dados.keys()]
	#prices = [obj. for obj in alunoBd]
	prices = [qtd for qtd in dados.values()]
	#reprov = [arped, arbd, arpoo, arcalc]
	#recup = [aerped, aerpbd, aerpoo, aercalc]

	context = {
	  'alunos': aluno,
	  'pagina': pagina,
	  'alunosAp': alunosAp,
	  'alunosRec': alunosRec,
	  'alunosRep': alunosRep,
	  'names': json.dumps(names),
	  'prices': json.dumps(prices),
	  #'reprov': json.dumps(reprov),
	  #'recup': json.dumps(recup),
	  #'total': alunos
	}
	print(context['names'])
	print(context['prices'])

	#print(context)
	return render(request, 'dashboard.html', context)

def clientes_ativo(request):
	print(request.get_full_path())
	pagina = str(request.get_full_path())
	return render(request, 'c_ativo.html', {'pagina': pagina})

@csrf_protect
def login(request):
	if request.POST:    
	    username = request.POST['username']
	    password = request.POST['password']
	    print(username)
	    print(password)
	    user = authenticate(username=username, password=password) #autentica o usuario
	    if user is not None: 
	    	dj_login(request, user) #loga
	    	if 'next' in request.POST:
	    		return redirect(request.POST['next'])
	    	else:	
	    		return redirect('/dashboard') #redireciona para o dash board
	    else:	  		
	    	messages.error(request, 'Usuário ou senha incorretos!')
	    	return redirect('/dashboard')
	else:
		return render(request, 'login.html')

def logout_user(request):
	print(request.user)
	logout(request)
	return redirect('/login')
	
@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno', raise_exception=True)
def alunos(request):
	alunos = Aluno.objects.all()
	pagina = str(request.get_full_path())
	print(pagina)
	contexto = {
		'alunos': alunos,
		'pagina': pagina
	}
	return render(request, 'alunos.html', contexto)

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno', raise_exception=True)
def editar(request, id):
	print(id)
	aluno = Aluno.objects.get(matricula=id)
	if request.POST:
		form = FormAluno(request.POST, instance=aluno) #instancia o com os dados existentes do aluno
		if form.is_valid():
			form.save()
			return redirect('/alunos/todos')
	else:
		form = FormAluno(instance=aluno)
		return render(request, 'editar.html', {'form':form})

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def editarPontuacao(request, id):
	print(id)
	aluno = Aluno.objects.get(matricula=id)
	if request.POST:
		form = FormAluno(request.POST, instance=aluno) #instancia o com os dados existentes do aluno
		if form.is_valid():
			form.save()
			return redirect('/alunos/todos')
	else:
		form = FormAluno(instance=aluno)
		return render(request, 'editar.html', {'form':form})
		
@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.add_aluno', raise_exception=True)
def novo(request):
	# form = FormAluno(request.POST or None)
	# if request.POST:
	# 	aluno = Aluno.objects.filter(nome=request.POST['nome'])
	# 	if aluno:
	# 		return HttpResponse('<strong>Aluno ja existe, tente outro</strong>')
	# 	elif form.is_valid():
	# 		form.save()
	# 		return redirect('/alunos/todos')
	# else:
	# 	return render(request, 'novo.html', {'form':form})
	turma = Turma.objects.all()	
	novo = Aluno()
	user = User()
	if request.POST:
		# aluno = Aluno.objects.filter(nome=request.POST['usuario'])
		user_existente = User.objects.filter(username=request.POST['usuario'])
		semestre = Turma.objects.filter(cod_turma=request.POST['semestre']).get()
		if not user_existente:
			user.username = request.POST['usuario']
			user.email = request.POST['email']
			user.set_password(request.POST['senha'])
			user.first_name = request.POST['p_nome']
			user.last_name = request.POST['u_nome']
			user.is_staff = True
			user.save()
			user = User.objects.last()
			user.groups.add(3) #adiciona o aluno no grupo de alunos
			user.save()

			novo.nome = user.get_full_name()
			novo.data_nac = request.POST['data']
			novo.user = user 
			novo.semestre = semestre
			novo.save()
			return redirect('/alunos/todos')
		else:
			return HttpResponse('Aluno ja existe')
	else:
		context = {'semestres': turma}
		return render(request, 'novo.html', context) 

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def pontuar_alunos(request, diciplina):
	# form = FormAluno_Diciplina(request.POST or None)
	# if request.POST:
	# 	if form.is_valid():
	# 		f = form.save()
	# 		print(dir(f))
	# 		calcMedia(request, f) #passando a request e os dados do form que foram enviados via POST
	# 		return redirect('/alunos/aprovados')
	# else:
	# 	return render(request, 'pontuar.html', {'form':form})
	dici = Aluno_Diciplina()
	total = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina=diciplina)
	alunos = Aluno.objects.all()
	di = Diciplina.objects.get(nome_diciplina=diciplina)
	if request.POST:
		aluno = Aluno_Diciplina.objects.filter(aluno_id=request.POST['aluno']).filter(diciplina__nome_diciplina=diciplina)
		print(aluno)
		if not aluno:
			if total.count() <= 20:
				dici.aluno_id = request.POST['aluno']
				dici.diciplina = di
				dici.n1 = request.POST['n1']
				dici.n2 = request.POST['n2']
				dici.n3 = request.POST['n3']
				dici.faltas = request.POST['faltas']
				dici.save()
				f = Aluno_Diciplina.objects.last()
				calcMedia(request, f, di)
				messages.success(request, 'Aluno matriculado com sucesso')
				return redirect('/minhasdiciplinas/{}'.format(diciplina))
			else:
				messages.error(request, 'Limite da turma alcançado')
				return render(request, 'pontuar.html', {'alunos':alunos})
		else:
			messages.error(request, 'Aluno já está matriculado nessa diciplina.')
			return render(request, 'pontuar.html', {'alunos':alunos})
	else:
		return render(request, 'pontuar.html', {'alunos':alunos})

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.delete_aluno', raise_exception=True)
def excluir(request, id):
	print(id)
	aluno = Aluno.objects.get(pk=id)
	if request.POST:
		Aluno.objects.get(pk=id).delete()
		return redirect('/alunos/todos')
	else:
		return render(request, 'excluir.html', {'aluno':aluno})

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def alunos_aprovados(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Aprovado').order_by('aluno')
	status = 'aprovados'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def alunos_reprovados(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Reprovado')
	status = 'reprovados'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)

@login_required(login_url='/login') #verifica o usuario
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def alunos_recuperacao(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Recuperação')
	status = 'em recuperação'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)

@login_required(login_url='/login')
def user_config(request):
	#user = User.objects.all()
	return render(request, 'config_user.html')#, {'user': user})

@login_required(login_url='/login')
def users(request):
	user = User.objects.all()
	if not request.user.is_superuser: #necessita ser superuser
		raise PermissionDenied
    
	return render(request, 'usuarios.html', {'usere': user})

@login_required(login_url='/login')
def users_perfil(request, user):
	usuario = get_object_or_404(User, username=user)
	print(usuario)
	if request.user.is_superuser:
		if request.POST:
			usuario.email = request.POST['email']
			usuario.first_name =  request.POST['primeiro']
			usuario.last_name = request.POST['ultimo']
			usuario.save()
			messages.success(request, 'Dados atualizados com sucesso!')
			return render(request, 'contas_usuarios.html', {'usuario': usuario})
		else:
			return render(request, 'contas_usuarios.html', {'usuario': usuario})
	else:
		raise PermissionDenied

@login_required(login_url='/login')
def redefinir_senha(request, user):
	usuario = get_object_or_404(User, username=user)
	
	if not request.user.username  == user:
		raise PermissionDenied

	print(usuario)
	if request.POST:
		senha_atual = request.POST['senha_atual']
		nova_senha = request.POST['nova_senha']
		nova_senha_conf = request.POST['nova_senha_conf']
		if usuario.check_password(senha_atual): #se a senha atual existe 
			if nova_senha == nova_senha_conf: # se a nova senha é igual a confirmada
				usuario.set_password(nova_senha) # converte o hash da senha para salvar
				usuario.save()
				messages.success(request, 'Senha alterada com sucesso!')
				return render(request, 'redefinir_senha.html')
			else:
				messages.error(request, 'Senhas não coincidem!')
				return render(request, 'redefinir_senha.html')
		else:
			messages.error(request, 'Você digitou sua senha antiga errada, por favor digite novamente!')
			return render(request, 'redefinir_senha.html')
	else:
		return render(request, 'redefinir_senha.html')

@login_required(login_url='/login')
@permission_required('lanc_notas.view_aluno_diciplina', raise_exception=True)
def minhas_diciplinas(request):
	try:
		if request.user.professor:
			return render(request, 'minhas_diciplinas.html')
		#elif request.user.aluno:			
			
	except:
		aluno = Aluno_Diciplina.objects.filter(aluno__user = request.user)
		return render(request, 'aluno_minhas_diciplinas.html', {'aluno':aluno})
	else:
		raise PermissionDenied

@login_required(login_url='/login')
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def alunos_diciplina(request, diciplina):
	dici = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina=diciplina)
	contexto = {
		'diciplina':dici,
		'dici_get':diciplina
	}
	print(dici)
	return render(request, 'alunos_diciplinas.html', contexto)
@login_required(login_url='/login')
@permission_required('lanc_notas.view_aluno_diciplina', raise_exception=True)
def diciplina(request, diciplina):
	if diciplina.isnumeric():
		return redirect('/minhasdiciplinas/{}/view'.format(diciplina))
	dici = Diciplina.objects.get(nome_diciplina=diciplina)
	alunos = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina=diciplina)
	contexto = {
		'diciplina':dici
	}
	if request.POST:
		dici.cod_diciplina = dici.cod_diciplina
		dici.nome_diciplina = dici.nome_diciplina
		dici.nota_aprovacao = dici.nota_aprovacao
		if request.POST['botao'] == 'Abrir':
			dici.semestre_aberto = True
			for a in alunos:
				a.renovar()
		else:
			dici.semestre_aberto = False
		dici.save()
		calcular_medias(request, diciplina)
		return redirect('/minhasdiciplinas/{}'.format(diciplina))
	else:
		return render(request, 'diciplina.html', contexto)
@login_required(login_url='/login')
@permission_required('lanc_notas.change_aluno_diciplina', raise_exception=True)
def editar_pontuacao(request, diciplina, id_aluno):
	#aluno = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina=diciplina).filter(id=id_aluno)
	aluno = get_object_or_404(Aluno_Diciplina, diciplina__nome_diciplina=diciplina, id=id_aluno)

	contexto = {
		'aluno':aluno,
	}
	print(aluno)
	if aluno.diciplina.semestre_aberto:
		if request.POST:
			aluno.aluno = aluno.aluno
			if not aluno.n1 and aluno.diciplina.semestre_aberto:
				aluno.n1 = request.POST['n1']
			if not aluno.n2 and aluno.diciplina.semestre_aberto:			
				aluno.n2 = request.POST['n2']
			if not aluno.n3 and aluno.diciplina.semestre_aberto:			
				aluno.n3 = request.POST['n3']
				
			aluno.faltas = request.POST['faltas']
			aluno.save()
			aluno.definir_situacao(aluno.diciplina.nome_diciplina)
			return redirect('/minhasdiciplinas/{}/alunos'.format(diciplina))
		else:	
			return render(request, 'frequencia.html', contexto)		
	else: 
		messages.error(request, 'Diciplina está fechada')
		return render(request, 'frequencia.html', contexto)		

@login_required(login_url='/login')
@permission_required('lanc_notas.view_aluno', raise_exception=True)
def notas_alunos(request, inscricao):
	aluno = Aluno_Diciplina.objects.get(id=inscricao)
	print('notas_alunos')
	return render(request, 'notas_alunos.html', {'aluno':aluno})

@login_required(login_url='/login')
@permission_required('lanc_notas.view_aluno', raise_exception=True)
def nova_matricula(request):
	aluno = Aluno_Diciplina.objects.filter(aluno__matricula=request.user.aluno.matricula)
	diciplina = Diciplina.objects.all()
	for a in aluno:
		diciplina = diciplina.exclude(nome_diciplina = a.diciplina)
	context = {'diciplina':diciplina}
	if request.POST:
		dici = Diciplina.objects.get(cod_diciplina=request.POST['diciplina'])
		total = Aluno_Diciplina.objects.filter(diciplina__nome_diciplina=dici)
		aluno = Aluno_Diciplina.objects.filter(aluno_id=request.user.aluno).filter(diciplina__nome_diciplina=dici)
		if dici.semestre_aberto:
			if aluno:
				messages.error(request, 'Aluno já está matriculado nessa diciplina')
				return render(request, 'nova_matricula.html', context)	
			if total.count() <= 20:
				novo = Aluno_Diciplina()		
				novo.aluno = request.user.aluno
				novo.diciplina = dici
				novo.definir_situacao(dici.nome_diciplina)
				novo.save()				
				messages.success(request, 'Você foi matriculado com sucesso em {}'.format(dici.nome_diciplina))
				return redirect('/minhasdiciplinas')	
			else:
				messages.error(request, 'Limite de alunos total alcançado, espere até o próximo periodo')
				return render(request, 'nova_matricula.html', context)
		else:
			messages.error(request, 'Semestre está fechado, impossivel a matricula fora do periodo')
			return render(request, 'nova_matricula.html', context)
	else:
		return render(request, 'nova_matricula.html', context)

@login_required(login_url='/login')
@permission_required('lanc_notas.add_aluno_diciplina', raise_exception=True)
def inscrever_em_diciplina(request):
	prof = Professor.objects.all()
	prof_select = Professor.objects.get(user__pk=request.user.professor.id)
	diciplina = Diciplina.objects.all()
	lista = []
	for p in prof: #para cada professor
		for a in p.diciplinas.all(): #para diciplina em professor com varias diciplinas
			lista.append(a) #adiciona em uma lista

	for l in lista: # para cada item da lista faz
	 	diciplina = diciplina.exclude(nome_diciplina = l) #faz 
	context = {'diciplina':diciplina}
	if request.POST:
		diciplina = request.POST['diciplina']
		prof_select.diciplinas.add(diciplina)
		return redirect('/minhasdiciplinas')
	else:
		return render(request, 'nova_matricula.html', context)

@login_required(login_url='/login')
@permission_required('lanc_notas.delete_aluno_diciplina', raise_exception=True)
def remover_diciplina(request, diciplina):
	diciplina = Diciplina.objects.get(nome_diciplina=diciplina)
	prof = Professor.objects.get(user__pk=request.user.pk)
	prof.diciplinas.remove(diciplina.pk)
	return redirect('/minhasdiciplinas')