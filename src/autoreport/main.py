from pathlib import Path

from autoreport.reader import ler_vendas
from autoreport.validator import validar_vendas
from autoreport.processor import processar_vendas
from autoreport.report import gerar_relatorio

def main() -> None:
    raiz_projeto = Path(__file__).resolve().parents[2]
    caminho_csv = raiz_projeto / "data" / "input" / "vendas.csv"

    # Lê o arquivo de vendas.
    vendas = ler_vendas(caminho_csv)

    # Valida os registros e separa os válidos dos inválidos.
    validas, invalidas = validar_vendas(vendas)

    # Processa as vendas válidas.
    vendas_processadas = processar_vendas(validas)

    # Define o caminho do relatório.
    caminho_relatorio = (
            raiz_projeto
            / "data"
            / "output"
            / "relatorio_vendas.xlsx"
    )

    # Gera o relatório Excel.
    gerar_relatorio(
        vendas_processadas,
        invalidas,
        caminho_relatorio,
    )

    print(f"\nRelatório gerado em: {caminho_relatorio}")

    # Exibe o resumo da validação.
    print("Validação concluída!")
    print(f"Total de registros: {len(vendas)}")
    print(f"Registros válidos: {len(validas)}")
    print(f"Registros inválidos: {len(invalidas)}")

    # Exibe os registros que apresentaram problemas.
    if not invalidas.empty:
        print("\nRegistros com problemas:")
        print(invalidas.to_string(index=False))

    print("\nVendas processadas:")
    print(vendas_processadas.to_string(index=False))


if __name__ == "__main__":
    main()