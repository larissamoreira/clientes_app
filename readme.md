Um simples CRUD :blush:

* Django :heavy_check_mark:
* Bootstrap :heavy_check_mark:
* API ViaCep :heavy_check_mark:
* CRUD :heavy_check_mark:
* Google Maps
* Cadastro/Login com Facebook
* Postgres :heavy_check_mark:
* Heroku :heavy_check_mark:

# Orientações gerais

## Django

* Primeiro, faça o download do código fonte: `git clone https://github.com/larissamoreira/clientes_app.git`

* Crie um ambiente virtual para instalar as dependências do projeto: `virtualenv ambiente` e depois o ative com `ambiente\Scripts\activate`

Você verá algo assim:
```
(ambiente) C:\Users\Larissa\teste>
```
* Agora precisamos instalar todas as dependências necessárias para o código funcionar, para isso entre no arquivo do projeto `cd clientes_app` e faça:
```
pip install -r requirements.txt
```

## Criando o banco

* Faça download do postgres em: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
* Abra o terminal e crie um usuário postgres com `psql -U postgres`
* Crie seu usuário com `CREATE USER <seu-username> WITH PASSWORD '<sua-senha>';`
* Crie o database com `CREATE DATABASE <nome-database> WITH OWNER <seu-username>;`
* Banco no postgres criado! Agora faça a conexão com o django no arquivo `settings.py` localizado no diretório myproject, para isso mude a variável `DATABASES` de acordo com o exemplo abaixo, adicionando suas informações do postgres.

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<nome-database>',
        'USER': '<seu-username>',
        'PASSWORD': '<sua-senha>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

* No diretório do projeto faça um `python manage.py makemigrations`
* Agora faça `python manage.py migrate`
* Para acessar o django-admin, crie um superuser com `python manage.py createsuperuser`
* Agora podemos rodar a aplicação com `python manage.py runserver`
* Acesse o endereço: http://127.0.0.1:8000/


