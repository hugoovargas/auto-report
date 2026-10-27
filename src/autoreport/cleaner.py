import pandas as pd

CATEGORIAS_PADRONIZADAS = {
    "perifericos": "Periféricos",
    "periféricos": "Periféricos",
    "acessorios": "Acessórios",
    "acessórios": "Acessórios",
    "audio": "Áudio",
    "áudio": "Áudio",
    "monitores": "Monitores",
    "moveis": "Móveis",
    "móveis": "Móveis",
}


def padronizar_colunas(dados: pd.DataFrame) -> pd.DataFrame:
    dados = dados.copy()

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

def padronizar_textos(dados: pd.DataFrame) -> pd.DataFrame:
    dados = dados.copy()

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

def padronizar_categorias(vendas: pd.DataFrame) -> pd.DataFrame:
    dados = vendas.copy()

    if "categoria" not in dados.columns:
        return dados

    dados["categoria"] = (
        dados["categoria"]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.casefold()
        .replace(CATEGORIAS_PADRONIZADAS))

    return dados


def limpar_vendas(vendas: pd.DataFrame) -> pd.DataFrame:
    dados = padronizar_colunas(vendas)

    dados = padronizar_textos(dados)

    dados = padronizar_categorias(dados)

    return dados