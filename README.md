# Projeto de gerenciamento acadêmico com Django 
Gerenciador academico para a administração de notas dos alunos. O sistema disponibiliza 3 níveis de acesso Alunos, Professores e Super user(onde esse tem permissao total no sistema)

# Instalação
1 - No seu computador instale o Python
2 - Crie uma venv "python -m venv venv"
3 - Ative "venv/Scripts/activate.bat"
4 - navegue até dentro da pasta do projeto e use "pip install -r requerements.txt" assim instala-rá todas as dependências
5 - rode "python manage.py createsuperuser" e escreva tudo que for pedido depois dê um "python manage.py makemigrations e depois migrate"

Pronto assim você poderá testar o nosso sistema

# Começando do zero
Você também pode apagar o banco de dados no Sqlite3 e logo em seguida rodar o comando "python manage.py createsuperuser" e escreva tudo que for pedido depois dê um "python manage.py makemigrations e depois migrate"
