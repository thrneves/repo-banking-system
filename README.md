# repo-banking-system

Sistema bancário em linha de comando — desafio do bootcamp **DIO**.
Implementa as operações básicas de depósito, saque e extrato sobre uma única conta em memória.

## Requisitos

- Python 3.10+ (uso de `dict | None`)

## Como executar

```bash
python main.py
```

O menu interativo aceita:

| Opção | Ação      |
|-------|-----------|
| `d`   | Depositar |
| `s`   | Sacar     |
| `e`   | Extrato   |
| `q`   | Sair      |

## Regras

- Saque limitado a **R$ 500,00** por operação.
- Máximo de **3 saques** por execução.
- É necessário realizar ao menos um depósito antes de sacar ou consultar o extrato.

## Estrutura

```
.
├── main.py                 # entrypoint, loop do menu
├── functions/
│   ├── deposits/           # depósitos
│   ├── withdrawals/        # saques (com limites)
│   └── extracts/           # impressão de extrato
└── base_code/desafio.py    # versão original do desafio (pt-BR), mantida como referência
```

## Convenção de chamada das funções

A passagem de argumentos foi padronizada de forma **intencional**, seguindo orientação do enunciado do desafio:

- **`deposits(account)`** — argumentos passados **por posição** (positional-only). A assinatura usa `/` para forçar essa forma: `def deposits(account: dict | None = None, /)`.
- **`withdrawals(account=account)`** — argumentos passados **por nome** (keyword-only). A assinatura usa `*,` para forçar essa forma: `def withdrawals(*, account: dict)`.
- **`extracts(account["balance"], extract=account["extract"])`** — combina os dois estilos: `balance` por **posição** e `extract` por **nome**. A assinatura usa `/` e `*` na mesma definição: `def extracts(balance: float, /, *, extract: str)`.

A diferença entre as chamadas é proposital — o objetivo do exercício é praticar ambas as formas de passagem de parâmetros em Python, e não uma inconsistência de estilo. Cada função impõe sua convenção via assinatura (`/` e `*`), de modo que o uso "errado" gera erro em tempo de execução.

## Próximos passos

- Mover os limites de saque (`limit`, `number_of_withdrawals`, `WITHDRAWAL_LIMIT`) em `functions/withdrawals/withdrawals.py` para variáveis de ambiente, evitando valores hardcoded.

## Licença

[MIT](LICENSE)
