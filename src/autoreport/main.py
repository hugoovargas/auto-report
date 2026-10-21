from pathlib import Path

from autoreport.reader import ler_vendas

def main() -> None:
    raiz_projeto = Path(__file__).resolve().parents[2]
    caminho_csv = raiz_projeto / "data" / "input" / "vendas.csv"

    vendas = ler_vendas(caminho_csv)

    print("Dados carregados com sucesso!")
    print()
    print(vendas)
    print()
    print(f"Total de registros: {len(vendas)}")


if __name__ == "__main__":
    main()
