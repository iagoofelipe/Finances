# API
Para o processamento de dados, foi construída uma API em Python 3.13, utilizando Django REST Framework. Para autenticação, a API utiliza `token JWT`, o qual está presente nas rotas de dados sensíveis.

# Rotas
Rotas disponíveis na API, junto aos seus métodos e parâmetros.

## /auth/

### POST
Utilizado para gerar o `token JWT`.

#### Parâmetros
| Nome | Tipo | Obrigatório | Valor Padrão | Descrição |
| --- | --- | --- | --- | --- |
| username | str | sim | - | Nome de usuário |
| password | str | sim | - | Senha do usuário |

#### Response
| Código | Retorno | Descrição |
| --- | --- | --- |
| 200 | [Token](#token) | dados do token |

## /reg

## /reg/all
Realiza a consulta dos registros. `token JWT` necesário.

### GET
Retorna todos os registros de acordo com os parâmetros fornecidos.

#### Parâmetros
| Nome | Tipo | Obrigatório | Valor Padrão | Descrição |
| --- | --- | --- | --- | --- |

#### Response
| Código | Retorno | Descrição |
| --- | --- | --- |
| 200 | [Registry[]](#registry) | registros associados aos parâmetros |

## /reg/add

### POST
Criação de um novo registro, `token JWT` necessário.

#### Parâmetros
Parâmetros de [RegistryRequest](#registryrequest), exceto `id`. `cardId` e `categoryId` são opcionais - caso passados, serão validados.

#### Response
| Código | Retorno | Descrição |
| --- | --- | --- |
| 200 | [Registry](#registry) | novo registro |
| 400 | [Error](#error) | erro de processamento |

Erros possíveis para a requisição.

| Nome | Descrição |
| --- | --- |
| `INVALID_ID` | caso `cardId` ou `categoryId` não sejam válidos |


## /reg/update
Atualiza os valores do registro.

### POST

#### Parâmetros
Parâmetros de [RegistryRequest](#registryrequest). Todos os parâmetros são opcionais, exceto `id`. Apenas os campos fornecidos serão atualizados.

#### Response
| Código | Retorno | Descrição |
| --- | --- | --- |
| 200 | [Registry](#registry) | novo registro |
| 400 | [Error](#error) | erro de processamento |

Erros possíveis para a requisição.

| Nome | Descrição |
| --- | --- |
| `INVALID_ID` | caso `id`, `cardId` ou `categoryId` não sejam válidos |

## /reg/delete

# Estruturas

Estruturas utilizadas pela API.

## Error
Erro de requisição.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| code | [ErrorCode](#errorcode) | código associado ao erro |
| error | str | descrição do erro |

## Card
Cartão bancário.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| id | str |
| number | str |

## Category
Categoria de registro.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| id | str |
| name | str |
| description | str |

## RegistryRequest
Registro de movimentação, utilizado para requests.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| id | str |
| title | str |
| value | decimal |
| datetime | str | Data e hora da criação do registro, seguindo o padrão `YYYY-MM-dd hh:mm:ss` |
| description | str |
| cardId | str|
| categoryId | str |

## Registry
Registro de movimentação.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| id | str |
| title | str |
| value | decimal |
| datetime | str | Data e hora da criação do registro, seguindo o padrão `YYYY-MM-dd hh:mm:ss` |
| description | str |
| card | [Card](#card) |
| category | [Category](#category) |

## Token
Dados do token gerado.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| refresh | str |
| access | str |

# Enumerações
Valores associados a um determinado objeto.

## ErrorCode
Erros retornados após o processamento.

| Nome | Valor | Descrição |
| --- | --- | --- |
| `AUTH_INVALID_CREDENTIALS` | 0 | usuário ou senha inválidos |
| `AUTH_INVALID_TOKEN` | 1 | token inválido ou ausente |
| `INVALID_ID` | 2 | id fornecido inválido |