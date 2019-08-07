"""gerencia_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lanc_notas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('calcular_medias', views.calcular_medias),
    path('dashboard', views.index),
    path('alunos/novo', views.novo),
    path('alunos/aprovados', views.alunos_aprovados),
    path('alunos/reprovados', views.alunos_reprovados),
    path('alunos/recuperacao', views.alunos_recuperacao),
    path('alunos/todos', views.alunos),
    path('alunos/editar/<int:id>', views.editar),
    path('alunos/pontuar/<str:diciplina>', views.pontuar_alunos),
    path('alunos/excluir/<int:id>', views.excluir),
    path('professores/inscrever', views.inscrever_em_diciplina),
    path('usuarios/perfil', views.user_config),
    path('usuarios', views.users),
    path('usuarios/<str:user>', views.users_perfil),
    path('usuarios/redefinirsenha/<str:user>', views.redefinir_senha),
    path('minhasdiciplinas', views.minhas_diciplinas),
    path('minhasdiciplinas/<str:diciplina>/alunos', views.alunos_diciplina),
    path('minhasdiciplinas/<str:diciplina>/<int:id_aluno>', views.editar_pontuacao),
    path('minhasdiciplinas/<str:diciplina>/', views.diciplina),
    path('minhasdiciplinas/<str:diciplina>/remover', views.remover_diciplina),
    path('minhasdiciplinas/<int:inscricao>/view', views.notas_alunos),
    path('novamatricula/', views.nova_matricula),
    path('login', views.login),
    path('logout', views.logout_user),

]
    
