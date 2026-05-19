# repo-banking-system

Sistema bancário em linha de comando — desafio do bootcamp **DIO**.
Permite cadastrar múltiplos clientes com validação de dados (CPF, data de nascimento, endereço), criar uma ou mais contas por cliente e realizar operações de depósito, saque e extrato em cada conta, mantidas em memória durante a execução.

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
| `a`   | Ações da conta (depósito, saque, extrato)     |
| `q`   | Sair                                          |

### Menu de cadastro (acessado por `c`)

| Opção | Ação                     |
|-------|--------------------------|
| `c`   | Cadastrar novo cliente   |
| `q`   | Voltar ao menu principal |

### Menu de ações da conta (acessado por `a`, após informar o CPF do cliente e o número da conta)

| Opção | Ação      |
|-------|-----------|
| `d`   | Depositar |
| `s`   | Sacar     |
| `e`   | Extrato   |
| `q`   | Voltar    |

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

## Estrutura

O projeto é organizado por **domínio** (cliente e conta), não por tipo (classe/função):

```
.
├── main.py                       # entrypoint, loop do menu principal
├── clients/
│   ├── client.py                 # MakeClient: cadastro e validação de dados do cliente
│   └── customer_menu.py          # menu de cadastro de cliente
├── accounts/
│   ├── account.py                # create_account: cria nova conta para um cliente existente
│   ├── function_menu.py          # menu de ações da conta (depósito/saque/extrato)
│   ├── deposits/                 # depósitos
│   ├── withdrawals/              # saques (com limite por conta e contador)
│   └── extracts/                 # impressão de extrato
└── base_code/desafio.py          # versão original do desafio (pt-BR), mantida como referência
```

## Convenção de chamada das funções

A passagem de argumentos foi padronizada de forma **intencional**, seguindo orientação do enunciado do desafio:

- **`deposits(account)`** — argumentos passados **por posição** (positional-only). A assinatura usa `/` para forçar essa forma: `def deposits(account: dict, /) -> dict`.
- **`withdrawals(account=account)`** — argumentos passados **por nome** (keyword-only). A assinatura usa `*,` para forçar essa forma: `def withdrawals(*, account: dict)`.
- **`extracts(account["balance"], extract=account["extract"])`** — combina os dois estilos: `balance` por **posição** e `extract` por **nome**. A assinatura usa `/` e `*` na mesma definição: `def extracts(balance: float, /, *, extract: str)`.

A diferença entre as chamadas é proposital — o objetivo do exercício é praticar ambas as formas de passagem de parâmetros em Python, e não uma inconsistência de estilo. Cada função impõe sua convenção via assinatura (`/` e `*`), de modo que o uso "errado" gera erro em tempo de execução.

## Licença

[MIT](LICENSE)
