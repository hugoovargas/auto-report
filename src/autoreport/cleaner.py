import pandas as pd

def padronizar_colunas(dados: pd.DataFrame) -> pd.DataFrame:
    dados.columns = (
        dados.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[\s-]+", "_", regex=True)
    )

    if dados.columns.duplicated().any():
        duplicadas = dados.columns[dados.columns.duplicated()].tolist()
        raise ValueError(f"Colunas Duplicadas após padronização: {duplicadas}")

    return dados

def padronizar_texto(dados: pd.DataFrame) -> pd.DataFrame:
    for coluna in ["produto", "categoria"]:
        if coluna in dados.columns:
            dados[coluna] = (
                dados[coluna]
                .astype("string")
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.casefold()
            )

        dados[coluna] = dados[coluna].replace("", pd.NA)

    return dados

def limpar_vendas(vendas: pd.DataFrame) -> pd.DataFrame:
    dados = vendas.copy()

    dados = padronizar_colunas(dados)

    dados = padronizar_texto(dados)

    return dados