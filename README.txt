Pequeno projeto de cadastro de fornecedores.

CLIENTES
============

Deve armazenar em banco de dados informações basicas sobre os clientes. Deve usar um modelo orientado a objetos. A interface de usuario deve possuir meios de inserção, leitura, atualização e esclusão dos fornecedores.


Modelo
------

- Nome fantasia
- Razão Social
- Telefone

Suporte
-------

Aplicação necessita de acesso remoto para suporte.


DJANGO
======

Python web framework cria projetos configuraveis atravez de um arquivo settings.py 
E permiti a criação de applicações plugaveis no projeto.

Se você possui python instalado e presente na variavel de ambiente PATH. Digite python --version versão desejada 3.6.X (caso não tenha recomendo Winpython)

Ambiente Virtual
----------------
Os pacotes do python são atualizados com frequência e as novas versões podem não ser retro compativeis. Para manter e testar varias versões dos mesmo pacote utilizamos 
ambientes virtutais, uma micro distribuição somente com os pacotes necessarios para aplicação atual. Python 3 já pussui o venv instalado. Na linha de comando digite:

python -m venv env    # env é o nome do ambiente como crio new.bat para iniciar o ambiente mais rapido sempre uso o mesmo nome "env"

ativar o ambiente:
.\env\scripts\activate   # o script new.bat ativa o ambiente caso o nome do ambiente seja env



Criando o projeto
-----------------
Primeiro instalar django:

pip install django   # o pip e o gerenciador de modulus do python e baixa e instala no ambiente python atual se estiver ativo

O django disponibiliza o script django-admin com o qual iniciamos um projeto

django-admin startproject startup    # startup é p nome do projeto

- startup
  |- startup
  | | __init__.py    # arquivo normalmente vazio indica ao python que a pasta é um modulo python
  | | settings.py    # arquivo de configuração do projeto django
  | | urls.py        # urls globais da aplicação
  | | wsgi.py	     # Web Server Gateway Interface
  | manage.py        # Scripty de gerenciamento do projeto


Settings
--------
O projeto django vem configurado para sqlite mais tem backends para a maioria dos bancos SQL via SQLAlquemy existe modulos django nosql para outros bancos.

Vamos testar. Com ambiente ativo e na pasta principal do projeto.

python manage.py migrate  # O django precisa de algumas tabelas no banco de dados para rodar o comando migrate cria as tabelas de todos app em INSTALLED_APPS em settings.py
python manage.py runserver  # django vem com um servidor de desenvolvimento e va disponibilisar a aplicação no IP loopback na porta 8000  => 127.0.0.1:8000


PRIMEIRO APP
============

python manage.py startapp cliente

cliente
| - migrations
| __init__.py
| admin.py        # disponibiliza o app no admin do django
| apps.py	  # da um nome unico a aplicação caso ocorra de haver app com o mesmo nome
| models.py	  # os objetos criados aqui seram salvos no banco de dados
| test.py	  # os teste automatizados da aplicação
| views.py	  # cria a logica de exibiçao dos modelos


Models
------
Os modelos do django herdam da classe models.Model e seu atributos de models.[field tipe]
Após criar as classes temos que ir no arquivo settings.py e adicionar o app cliente na lista de INSTALLED_APP e criar as migrações

python manage.py makemigrations # na pasta migrations de cliente haverá um arquivo 0001_initial.py de criaçao das tabelas

Views
-----
Django possui classe para visões genericas em forma de classe que nossas views podem herdar.
Client List, Detail, Create, Update, Delete


Templates
---------
Por ser um framework web as exibição do django é atravez de um template html.
Primeiro precisamos de um template base cujo outros templates vão extender.
Como a aplicaçao deve ser plugável utilizada em outros projetos ela não deve conter essa base pois isso é a aparencia do projeto.
Por ser um template simples vou colocar o base.html na pasta templates de startup caso seu projeto creça podemo criar um app para o design do site.

Arquivos staticos:
Cirada pasta static em startup e esse arquivos seram servidos pelo django atravez da template tag {% static %}

No base.html temos alem de conteudo padrão html e css temos o {% load %} and {% block %} onde o django incluira sua logica.

Vamos criar na app cliente na pasta templates o:
- client_list.html
- client_delete.html
- client_datail.html
- client_crete.html
- client_update.html

Urls
----
Precisamos criar as urls os caminho que vão levar as diferentes visões da applicação e seus templates. urls.py
Essa urls são tambem devem ser incluidas no arquivos de urls.py do projeto atravez do include.

Agora podemos iniciar o servidor de desenvolvimento para usar a aplicaçao:

python manage.py migrate       # Já haviamos criado as migrações do modelo mas não execultamos elas
python manage.py collectstatic # reune todos os arquivos staticos que em produçao seram servidos separadamente
python manage.py runserver
