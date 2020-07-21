> Projeto prático desenvolvido na aceleração Python Online da Codenation, com apoio da Stone
# Centralizador de Erros - Backend (API)
Este projeto consiste de uma API RESTful para submissão de log de erros em um centralizador que deve concentrar os erros de diferentes aplicações e das diferentes camadas dessas aplicações.

## Principais tecnologias
- [Python](https://www.python.org)`3.8.2`
- [Django](https://www.djangoproject.com)`3.0.8`
- [Django REST framework](https://www.django-rest-framework.org)`3.11.0`
- [Swagger](https://www.swagger.io)`2.0`

## Replicação local
### Clonando o repositório
`$ git clone https://github.com/AlefCS/CentralErros_AceleraDev`
### Criação e ativação do ambiente virtual (opcional)
Esta parte é opcional, mas é recomendado que você utilize um ambiente virtual. Fica a cargo de cada um escolher o ambiente virtual de sua preferência. Aqui mostrarei como criar e preparar o ambiente virtual utilizado durante o desenvolvimento deste projeto (`virtualenv`). Primeiramente entre na pasta do projeto que acabou de ser clonado.

`$ cd CentralErros_AceleraDev`

Instale o `virtualenv`.

`$ pip install virtualenv`

Agora crie o ambiente virtual com o seguinte comando, lembrando de substituir `<VENV_NAME>` por um nome de sua escolha.

`$ virtualenv <VENV_NAME> -p python3`

Por fim, ative o ambiente virtual criado.

`$ source <VENV_NAME>/bin/activate`

### Instalação dos pré-requisitos
`$ pip install -r requirements.txt`
> Nota: os pacotes `dj_database_url`, `psycopg2-binary`, `whitenoise` e `gunicorn` apenas foram utilizados para realizar o _deploy_ da aplicação. Sendo assim, caso queira, você pode removê-los do arquivo `requirements.txt` ou então desinstalá-los a qualquer momento.

### Gerando chave secreta do Django
Abra o interpretador do python e use o _script_ abaixo para gerar a chave do Django.
```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

### Atualizando chave secreta do Django
Abra o arquivo `settings.py` que está dentro da pasta `errors_center/`. Procure a linha contendo `SECRET_KEY = os.environ['DJANGO_SECRET_KEY']` e substitua por `SECRET_KEY = "<GENERATED_SECRET_KEY>"`, em que `<GENERATED_SECRET_KEY>` é a chave que foi gerada no passo anterior.

### Inicialização do banco de dados
`$ python manage.py migrate`

### Criando super usuário
`$ python manage.py createsuperuser`

Após rodar esse comando será requisitado um nome de usuário, email (ex.: <span>qualquer@</span>coisa.serve) e senha. Preencha essas informações e o super usuário será criado. Este é um usuário com permissões de administrador. Com ele será possível criar outros usuários e ter acesso à interface de administração do Django.

### Rodando a aplicação
`python manage.py runserver`

Pronto, agora a aplicação já está rodando e está pronta para uso. Você pode usar o super usuário criado no passo anterior para autenticação na API. Você pode acessar a interface de administração através da URL [localhost:8000/admin](http://localhost:8000/admin).

Para acesso à documentação e ter mais informações sobre como utilizar a API acesse [localhost:8000](http://localhost:8000).
> Nota 1: a documentação foi criada pensando na aplicação que está sendo hospedada no Heroku. Por isso, para acesso às funcionalidades do sistema que está rodando localmente você deve se lembrar de substituir `acs-errorscenter.herokuapp.com` por `localhost:8000` sempre que for necessário.

> Nota 2: o usuário/senha e _token_ fornecidos na documentação funcionam para aplicação que está sendo hospedada no Heroku e não deve funcionar no sistema local. Localmente, utilize os usuários que você criou e seus respectivos _tokens_.

## _Deploy_
Para demonstração da API, foi feito o _deploy_ da mesma no Heroku e esta pode ser acessada [clicando aqui](https://acs-errorscenter.herokuapp.com).
