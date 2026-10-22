from pathlib import Path

from autoreport.reader import ler_vendas
from autoreport.validator import validar_vendas
from autoreport.processor import processar_vendas

def main() -> None:
    raiz_projeto = Path(__file__).resolve().parents[2]
    caminho_csv = raiz_projeto / "data" / "input" / "vendas.csv"

    # Lê o arquivo de vendas.
    vendas = ler_vendas(caminho_csv)

    # Valida os registros e separa os válidos dos inválidos.
    validas, invalidas = validar_vendas(vendas)
    vendas_processadas = processar_vendas(validas)

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