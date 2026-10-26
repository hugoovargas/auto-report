import pandas as pd

def limpar_vendas(vendas: pd.DataFrame) -> pd.DataFrame:
    dados = vendas.copy()
    dados.columns = (
        dados.columns
        .str.strip()
        .str.lower()
    )

    for coluna in ["produto", "categoria"]:
        if coluna in dados.columns:
            dados[coluna] = (
                dados[coluna]
                .astype("string")
                .str.strip()
                .str.replace(r"/s+", " ", regex=True)
                .replace("", pd.NA)
            )

    return dados