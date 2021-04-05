# dry-rest-permission-ddd-example
Esse repositório foi feito para exemplificar o uso da lib 
dry-rest-permissions com uma arquitetura hexagonal/ddd.

## Lib
> https://github.com/FJNR-inc/dry-rest-permissions

> https://github.com/FJNR-inc/dry-rest-permissions/pull/15

> https://github.com/imobanco/dry-rest-permissions/tree/feature/get_permission_target

## DDD

> https://github.com/imobanco/drf-api-domain

demostração da arquitetura sugerida no
styleguide django-api-domains <https://phalt.github.io/django-api-domains>


# Instalação
## Docker + docker-compose
Instale [docker-ce](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) utilizando suas respectivas documentações.

> para rodar o docker sem utilizar o `sudo` no linux é 
> necessário executar o comando `sudo usermod -aG docker {seu_usuario}
> e depois reiniciar a sessão (logout/restart)

### Configurando
Todos os comandos devem ser chamados da pasta do projeto.

#### Variáveis de ambiente
Há um arquivo de exemplod e variáveis de ambiente, o `.env.example`. Com o comando abaixo é criaro o `.env` a partir dele:

```console
make config.env
```

#### Containers
Para dar build nos containers basta rodar o comando:
```console
make build
```

# Rodando o projeto
Basta rodar o comando

```console
make up.logs
```

Esse comando irá iniciar alguns serviçoes na sua máquina. São esses:
- Django server no endereço [http://0.0.0.0:8000](http://0.0.0.0:8000)
- PostgreSQL na porta [5432]()

## Populates
Para popular o BD com alguns cadastros iniciais rodar o
```shell script
make populate.superuser
```