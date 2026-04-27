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

## Próximos passos

- Mover os limites de saque (`limit`, `number_of_withdrawals`, `WITHDRAWAL_LIMIT`) em `functions/withdrawals/withdrawals.py` para variáveis de ambiente, evitando valores hardcoded.

## Licença

[MIT](LICENSE)
