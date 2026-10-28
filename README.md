# AutoReport

Aplicação desenvolvida em Python para automatizar a leitura, validação e análise de dados de vendas a partir de arquivos CSV, gerando relatórios em Excel com indicadores e informações consolidadas.

O projeto utiliza **pandas** para manipulação e análise dos dados e **openpyxl** para exportação de planilhas Excel.

## Funcionalidades

- Leitura de dados de vendas a partir de arquivos CSV.
- Padronização dos nomes das colunas.
- Limpeza de textos de produtos e categorias.
- Padronização de categorias conhecidas.
- Validação de campos obrigatórios.
- Identificação de IDs de venda duplicados.
- Validação de datas, quantidades e preços unitários.
- Separação de registros válidos e inválidos.
- Registro dos motivos de invalidação.
- Cálculo do faturamento individual de cada venda.
- Cálculo de indicadores gerais e consolidação do faturamento por produto e categoria.
- Geração de relatório Excel com abas para resumo, vendas processadas e registros inválidos.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **pandas** — leitura, limpeza, validação e análise dos dados.
- **openpyxl** — suporte à geração de arquivos Excel.
- **pytest** — execução dos testes automatizados.
- **Git** — controle de versão.

## Estrutura do projeto

```text
AutoReport/
├── data/
│   ├── input/
│   │   └── vendas.csv
│   └── output/
│       └── relatorio_vendas.xlsx
├── src/
│   └── autoreport/
│       ├── main.py
│       ├── reader.py
│       ├── cleaner.py
│       ├── validator.py
│       ├── processor.py
│       ├── metrics.py
│       └── report.py
├── tests/
├── .gitignore
└── README.md
```

## Como funciona

O processamento dos dados segue estas etapas:

1. **Leitura:** o programa carrega o arquivo `vendas.csv`.
2. **Limpeza:** padroniza nomes das colunas, textos de produtos e categorias.
3. **Validação:** verifica campos obrigatórios, IDs duplicados, datas, quantidades e preços, separando os registros válidos dos inválidos.
4. **Processamento:** calcula o faturamento de cada venda válida multiplicando a quantidade pelo preço unitário.
5. **Análise:** calcula indicadores gerais e agrupa o faturamento por produto e categoria.
6. **Exportação:** gera um relatório Excel com os resultados e os registros que apresentaram problemas.

## Indicadores gerados

O relatório apresenta os seguintes indicadores:

| Indicador | Descrição |
|---|---|
| Faturamento total | Soma do faturamento das vendas válidas. |
| Quantidade total vendida | Soma das quantidades das vendas válidas. |
| Número de vendas | Quantidade de registros válidos. |
| Faturamento por produto | Faturamento total agrupado por produto. |
| Faturamento por categoria | Faturamento total agrupado por categoria. |

## Relatório Excel

O arquivo gerado é `relatorio_vendas.xlsx`, salvo no diretório `data/output/`.

Ele contém três abas:

- **Resumo:** indicadores gerais, faturamento por produto e faturamento por categoria.
- **Vendas:** registros válidos após o processamento, incluindo o faturamento calculado.
- **Registros inválidos:** registros rejeitados durante a validação, acompanhados dos motivos identificados.

O programa cria o diretório de saída automaticamente quando necessário.

## Requisitos

- Python 3.10 ou superior.
- pandas.
- openpyxl.
- pytest para executar os testes.

## Instalação

Clone o repositório e entre no diretório do projeto:

```bash
git clone https://github.com/hugoovargas/auto-report.git
cd AutoReport
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install pandas openpyxl pytest
```

## Como utilizar

Coloque o arquivo CSV de entrada em:

```text
data/input/vendas.csv
```

O arquivo deve conter as colunas obrigatórias:

- `id_venda`
- `data`
- `produto`
- `quantidade`
- `preco_unitario`
- `categoria`

Execute o programa a partir da raiz do projeto:

```bash
PYTHONPATH=src python -m autoreport.main
```

Após a execução, o relatório estará disponível em:

```text
data/output/relatorio_vendas.xlsx
```

O terminal também apresenta um resumo da validação, com o total de registros, a quantidade de registros válidos e inválidos e os registros que apresentaram problemas.

## Executando os testes

Para executar os testes automatizados, utilize:

```bash
PYTHONPATH=src pytest -v
```

## Regras de validação

Atualmente, o programa considera inválidos os registros que apresentam:

- Campos obrigatórios vazios.
- IDs de venda duplicados.
- Datas ausentes ou que não podem ser interpretadas pelo pandas.
- Quantidades não numéricas, menores ou iguais a zero ou não inteiras.
- Preços unitários não numéricos, menores ou iguais a zero.

Os registros inválidos são preservados no relatório para facilitar a identificação e a correção dos problemas na origem.

## Objetivo do projeto

O AutoReport foi desenvolvido como projeto de portfólio para praticar Python, pandas, validação e transformação de dados, organização de código em módulos, testes automatizados e geração de relatórios para análise de informações comerciais.

O projeto demonstra um fluxo de automação de dados que pode ser aplicado a rotinas administrativas e operacionais, reduzindo tarefas manuais de consolidação de informações.

