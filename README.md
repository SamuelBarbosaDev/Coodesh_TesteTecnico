<h1>Spacex Challenge</h1>
<p>Fullstack Challenge 🏅 Space X API</p>
<p>...</p>

## URLS:
- [GET] /message
- [GET] /launches
- [GET] /stats
- /v1/api/swagger/
- /v1/api/doc/



## API:
```
https://api.spacexdata.com/v5/launches/latest
```

## Passo a Passo:

- Crie um ambiente virtual
```
python -m venv venv
```

- Ative o ambiente virtual
```
source venv/bin/activate
```

- instale as dependências
```
pip install -r requirements.txt
```

- Entre na pasta apps/
```
cd apps/
```

- excute as migrations
```
python manage.py migrate
```

- Crie um usuario admin
```
python manage.py createsuperuser --email admin@admin.com --username admin
```

- Crie sua senha
```
******
```

- Repita a senha
```
******
```

- Excute o projeto localmente, Fim.
```
python manage.py runserver
```

## Script / Comando customizado do Django:
Alimenta o banco de dados com os dados de lançamentos da SpaceX.

- Excute o comando para comsumi a api da SpaceX.
```
python manage.py store_launching_data
```