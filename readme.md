Um simples CRUD :blush:

* Django :heavy_check_mark:
* Bootstrap :heavy_check_mark:
* API ViaCep :heavy_check_mark:
* CRUD :heavy_check_mark:
* Google Maps
* Cadastro/Login com Facebook
* Postgres :heavy_check_mark:
* Heroku

# Orientações gerais

## Postgres

1. Faça download do postgres em: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
2. Abra o terminal e crie um usuário postgres com `psql -U postgres`
3. Crie seu usuário com `CREATE USER <seu-username> PASSWORD '<sua-senha>';`
4. Crie o database com `CREATE DATABASE <nome-database> WITH OWNER <seu-username>;`
5. Banco no postgres criado! Agora faça a conexão com o django em `settings.py`, para isso mude a variável `DATABASES` de acordo com o exemplo abaixo, adicionando suas informações do postgres.

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'nome-database'),
        'USER': os.environ.get('DB_USER', 'seu-username'),
        'PASSWORD': os.environ.get('DB_PASS', 'sua-senha'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}`

6. Faça um `python manage.py makemigrations`
7. Faça um `python manage.py migrate`

