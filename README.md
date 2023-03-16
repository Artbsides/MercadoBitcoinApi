# MercadoBitcoinApi

Aplicação CRUD desenvolvida em [Python 3.11.12](https://www.python.org), focada no gerenciamento de produtos.

# Armazenamento de Dados

Para fins de armazenamento de dados, esta aplicação faz uso de PostgreSQL como fonte de dados principal e Redis como fonte de dados em cache.

# Lógica Aplicada

Por se tratar de uma aplicação CRUD simples, a lógica existente está relacionada aos storages, sendo assim, toda ação é feita primeiramente em Redis ou em PostgreSQL dependendo do seu tipo, porém, sempre em ambos.

Segue abaixo o fluxo exemplificando operações de consulta.

```
[GET REQUEST/products/{id-do-produto}]
    |
    |-->[API verifica se registro existe em Redis]
            |
            |-->[Se sim, retorna dados do Redis]
            |-->[Se não, verifica se registro existe em PostgreSQL]
                    |
                    |-->[Se sim, retorna dados do PostgreSQL]
                    |-->[Se não, lança exception NotFound]

    |-->[Retorna dados/exception no formato json]
```

# Instalação

Esta aplicação foi desenvolvida sob linux utilizando de algumas ferramentas excenciais, sendo assim, é necessário instalar as dependências do projeto listadas abaixo para que seja possível subir todos os serviços para sua execução.

Dependências para execução dockerizada (necessário também para execução dos storages):

```
Make
Docker
```

Dependências para execução diretamente em máquina local (opcional):

```
Pip v23.0.1+
Python v3.11.2+
```

Após certificar-se de que as dependências estejam instaladas na máquina que irá executar esta aplicação, pode-se facilmente subir os serviços utilizando os comandos listados no arquivo Makefile.

Para execução da aplicão completamente dockerizada, não se faz necessária a instalação das dependências para exeução em máquina local.

# Makefile

O arquivo Makefile possui comandos pré-configurados que auxiliam algumas rotinas em ambiente dockerizado, tais como: disponibilizar banco de dados e cache, inicializar a aplicação, excução de testes e convenção de código, assim como também manipular arquivos contendo variáveis de ambiente encriptadas e tags no github.

Para exibir a relação de comandos disponíveis e seus respectivos modos de uso, basta aplicar um dos seguintes comandos:

```
$ make
$ make help
```

# Inicialização da Aplicação

A abordagem a partir deste ponto será voltada a disponibilização dos serviços e a iniciaização da aplicação de forma dockerizada. Para isso, é necessário que inicialmente as imagens a serem utilizadas no Docker sejam construídas.

Para a construção das imagens, aplique o comando abaixo:

```
$ make build
```

Após a construção das imagens, é necessário disponibilizar os storages. Para isso, aplique os comandos abaixo:

```
$ make redis
$ make postgres
```

Uma vez que os storages estejam disponíveis, é necessário aplicar a migração das tabelas no PostgreSQL, porém, pode ser necessário instalar as dependências do projeto antes disso, sendo assim, aplique os comandos abaixo:

```
$ make packages
$ make database-migrations
```

A partir deste ponto tudo o que é necessário já encontra-se devidamente instalado e disponível. Caso seja necessário executar testes e análise de código, os comandos abaixo devem ser utilizados:

```
$ make tests
$ make code-convention
```

Por fim, para inicializar a aplicação basta aplicar o seguinte abaixo:

```
$ make run mode=development|latest
```

Caso corra tudo conforme o esperado e nenhuma variável de ambiente tenha sido previamente modificada, a aplicação estará disponível na url: http://127.0.0.1:8000.
# Utilização

Esta aplicação foi implementada de forma modular e versionável, porém, até o momento não foram gerados arquivos para interação utilzando [Postman](https://www.postman.com), sendo assim, segue a lista de rotas existentes e suas formas de uso.

Criação de produtos:
```
$ curl --location 'http://127.0.0.1:8000/v1/products' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MTYyMzkwMjJ9.RHTJ6ziBOktHKqiGE-HhBQUrr-7gTJJDdAdg1-r38oI' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Product One"
}'
```

Leitura de produtos:
```
$ curl --location 'http://127.0.0.1:8000/v1/products/71befe2a-571e-4992-b3ae-c78ee77291ce' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MTYyMzkwMjJ9.RHTJ6ziBOktHKqiGE-HhBQUrr-7gTJJDdAdg1-r38oI'
```

Leitura de um único produto:
```
$ curl --location 'http://127.0.0.1:8000/v1/products' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MTYyMzkwMjJ9.RHTJ6ziBOktHKqiGE-HhBQUrr-7gTJJDdAdg1-r38oI'
```

Atualização de um único produto:
```
$ curl --location --request PATCH 'http://127.0.0.1:8000/v1/products/71befe2a-571e-4992-b3ae-c78ee77291ce' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MTYyMzkwMjJ9.RHTJ6ziBOktHKqiGE-HhBQUrr-7gTJJDdAdg1-r38oI'
```

Deleção de um único produto:
```
$ curl --location --request DELETE 'http://127.0.0.1:8000/v1/products/71befe2a-571e-4992-b3ae-c78ee77291ce' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5MTYyMzkwMjJ9.RHTJ6ziBOktHKqiGE-HhBQUrr-7gTJJDdAdg1-r38oI'
```

* É provável ser necessário substituir o token utilizado no header Authorization das requests acima.

# Variáveis de Ambiente

As variáveis de ambiente estão configuradas no arquivo .env e estão organizadas por tipo de uso, setadas para desenvolvimento local. Toda configuração é aplicada automaticamente tanto para inicialização em ambiente Docker quanto em máquina local.

Caso seja necessário alterar alguma variável, basta editá-las. As alterações serão aplicadas em todos os modos de inicialização.

* Lembre-se de atribuir valor à variável de ambiente JWT_SECRETS. Para gerar um token válido, acesse o site do JWT e altere a data de expiração utilizando a mesma chave de segurança configurada nas variáveis de ambiente (JWT_SECRETS) sem encodar em Base64.

```
| ----------------------------------- |
| Header                              |
| ----------------------------------- |
| {                                   |
|     "alg": "HS256",                 |
|     "typ": "JWT"                    |
| }                                   |
| ----------------------------------- |
| Payload                             |
| ----------------------------------- |
| {                                   |
|     "exp": 1686239022               |
| }                                   |
| ----------------------------------- |
| Verify Signature                    |
| ----------------------------------- |
| HMACSHA256(                         |
|     base64UrlEncode(header) + "." + |
|     base64UrlEncode(payload),       |
|     [ "secret" ]                    |
| ) [ ] secret base64 encoded         |
| ----------------------------------- |
```

Em ambientes externos voltados a staging e production, as variáveis de ambiente são encriptadas e estão localizadas no diretório .k8s, que também possui outras configurações para deploy em kubernetes.

Para encriptar e/ou desencripar as variáveis de ambiente de staging e production é necessario que o ambiente de infra esteja devidadamente alinhado com esta aplicação, porém, este recurso não será devidamente documentado neste repositório, ainda assim, caso seja de interesse das partes, notifique-me para a demonstração de uso.

# Workflows

Foram implementadas actions que são executadas em diferentes cenários com o objetivo de aplicar testes e análise de código, assim como também o deploy da aplicação.

Para que as actions relacionadas aos testes e análise de código sejam executadas, basta a realização do push para a branch na qual está recebendo modificações, caso as actions identifiquem problemas, o merge da branch junto a main não será permitido.

Quanto ao deploy, esta action utiliza workflows compartihados e assim como as variáveis de ambiente encriptadas e demais recursos de deploy, é necessário estar alinhado com o ambiente de infra, porém, a nível de explicação, para execução da action, basta criar tags e o processo inicializará.

# Melhorias Necessárias

* Formatação de erros e exceptions
* Injeção de dependência no controller de forma única
* Validar versionamento de rotas através de headers ao invés de url contendo versão
* Gerar rotas no Postman contendo exemplos de uso e retornos

# Pricipais Tecnologias Utilizadas

* [FasAPI](https://fastapi.tiangolo.com)
* [Alembic](https://alembic.sqlalchemy.org)
* [SqlAlchemy](https://www.sqlalchemy.org)
* [Redis](https://redis.io)
* [PostgreSQL](https://www.postgresql.org)
