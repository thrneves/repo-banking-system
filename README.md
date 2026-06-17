# repo-banking-system

Sistema bancário em linha de comando — desafio do bootcamp **DIO**.
Permite cadastrar múltiplos clientes com validação de dados (CPF, data de nascimento, endereço), criar uma ou mais contas por cliente e realizar operações de depósito, saque e relatório de transações em cada conta, mantidas em memória durante a execução.

## Requisitos

- Python 3.10+ (uso de `match/case`)

## Como executar

```bash
python main.py
```

### Menu principal

| Opção | Ação                                          |
|-------|-----------------------------------------------|
| `c`   | Cadastrar cliente (com validação dos dados)   |
| `n`   | Nova conta (para um cliente já cadastrado)    |
| `l`   | Listar clientes cadastrados                   |
| `i`   | Listar todas as contas do banco               |
| `a`   | Ações da conta (depósito, saque, relatório)   |
| `q`   | Sair                                          |

### Menu de cadastro (acessado por `c`)

| Opção | Ação                     |
|-------|--------------------------|
| `c`   | Cadastrar novo cliente   |
| `q`   | Voltar ao menu principal |

### Menu de ações da conta (acessado por `a`, após informar o CPF do cliente e o número da conta)

| Opção | Ação       |
|-------|------------|
| `d`   | Depositar  |
| `s`   | Sacar      |
| `r`   | Relatório  |
| `q`   | Voltar     |

> **Nota:** a opção de **extrato** (`e`) foi desativada. Comentei tudo do repositório
> que tinha a ver com a função `extracts` — o **gerador de relatórios** (`report_generator`)
> já é o suficiente para expressar os extratos de contas. O código da função `extracts`
> permanece no repositório apenas como referência de estudo.

## Regras

### Cadastro de cliente
- CPF: 11 dígitos, único por cliente.
- Data de nascimento: formato `dd/mm/aaaa`, validada como data real.
- Endereço: todos os campos são obrigatórios.
- Sigla do estado: exatamente 2 letras.

### Contas
- Cada cliente pode ter **uma ou mais contas**; cada conta pertence a um único cliente.
- Número da conta: gerado sequencialmente a partir de 1, incrementando a cada nova conta criada (independente de cliente).
- Agência: `0001` (valor fixo, conforme enunciado do desafio).
- Conta nova nasce com saldo zero e sem movimentações.

### Operações da conta
- Limite por saque definido em cada conta (campo `limit`, valor inicial **R$ 1.500,00**).
- Máximo de **3 saques** por conta durante a execução.
- Saque não pode exceder o saldo disponível.

### Relatório de transações
- Substitui o antigo extrato. Usa o **gerador** `report_generator`, que percorre as
  transações da conta com `yield`, permitindo filtrar por tipo (depósitos, saques ou todas).

## Estrutura

O projeto é organizado por **domínio** (cliente e conta), não por tipo (classe/função):

```
.
├── main.py                       # entrypoint, loop do menu principal
├── decorator.py                  # decorador @log: grava os registros de cada chamada em log.txt
├── clients/
│   ├── client.py                 # MakeClient: cadastro e validação de dados do cliente
│   └── customer_menu.py          # menu de cadastro de cliente
├── accounts/
│   ├── account.py                # create_account: cria nova conta para um cliente existente
│   ├── account_iterator.py       # ContaIterador: itera sobre todas as contas do banco
│   ├── function_menu.py          # menu de ações da conta (depósito/saque/relatório)
│   ├── deposits/                 # depósitos
│   ├── withdrawals/              # saques (com limite por conta e contador)
│   ├── reports/                  # report_generator: gerador que percorre as transações
│   └── extracts/                 # extracts (DESATIVADO — substituído pelo gerador de relatórios)
└── base_code/desafio.py          # versão original do desafio (pt-BR), mantida como referência
```

## Convenção de chamada das funções

A passagem de argumentos foi padronizada de forma **intencional**, seguindo orientação do enunciado do desafio:

- **`deposits(account)`** — argumentos passados **por posição** (positional-only). A assinatura usa `/` para forçar essa forma: `def deposits(account: dict, /) -> dict`.
- **`withdrawals(account=account)`** — argumentos passados **por nome** (keyword-only). A assinatura usa `*,` para forçar essa forma: `def withdrawals(*, account: dict)`.
- **`extracts(account["balance"], extract=account["extract"])`** — combina os dois estilos: `balance` por **posição** e `extract` por **nome**. A assinatura usa `/` e `*` na mesma definição: `def extracts(balance: float, /, *, extract: str)`.

A diferença entre as chamadas é proposital — o objetivo do exercício é praticar ambas as formas de passagem de parâmetros em Python, e não uma inconsistência de estilo. Cada função impõe sua convenção via assinatura (`/` e `*`), de modo que o uso "errado" gera erro em tempo de execução.

> O exemplo de `extracts` é mantido aqui apenas como referência de estudo: a função está
> desativada no sistema (ver nota no menu de ações da conta), mas continua sendo um bom
> exemplo de combinação de `/` e `*` na mesma assinatura.

## Iterador personalizado `ContaIterador`

O arquivo `account_iterator.py` define a classe `ContaIterador`, usada para praticar o
**protocolo de iterador** em Python (`__iter__` e `__next__`). Ela permite percorrer
**todas as contas do banco** de uma vez, independente de qual cliente é dono de cada conta.

```python
for conta in ContaIterador(clients_list):
    print(conta)  # {'owner': ..., 'agency': ..., 'number': ..., 'balance': ...}
```

Como as contas ficam guardadas **dentro de cada cliente** (`client["accounts"]`), o
`__init__` "achata" essa estrutura numa lista única de tuplas `(dono, conta)` — assim a
informação de quem é a conta não se perde. O `__next__` devolve as informações básicas de
cada conta (titular, agência, número e saldo) e levanta `StopIteration` quando chega ao fim.
É acessível pela opção `i` do menu principal.

## Decorador `@log`

O arquivo `decorator.py` define o decorador `log`, usado para praticar o conceito de **decoradores** em Python. A cada chamada da função decorada, ele registra os detalhes da execução em um arquivo `log.txt` (criado na raiz do projeto) em vez de imprimir no terminal:

```python
@log
def deposits(account: dict, /) -> dict:
    ...
```

Cada chamada gera uma linha no `log.txt` com o nome da função, o horário, os argumentos recebidos, o tipo do retorno e o próprio valor de retorno — por exemplo:

```
Running: deposits on 2026-06-17 08:39:17 - Arguments: ({'balance': 100, ...},) - Type: <class 'dict'>. Return: {...}
```

O arquivo é aberto em modo de **acréscimo** (`"a"`), de forma que os registros se acumulam a cada execução, e o caminho é resolvido a partir de `Path(__file__).parent` para gravar sempre na raiz do projeto. A escrita é protegida por um `try/except IOError`, que avisa no terminal caso haja falha ao manipular o arquivo. O decorador usa `functools.wraps` para preservar o nome e a documentação da função original e está aplicado às principais operações do sistema: cadastro de cliente (`client.py`), criação de conta (`account.py`), depósito e saque.

## Licença

[MIT](LICENSE)
