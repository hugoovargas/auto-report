import pandas as pd

def processar_vendas(vendas: pd.DataFrame,) -> pd.DataFrame:
    dados = vendas.copy()

    dados["faturamento"] = (
        dados["quantidade"] * dados["preco_unitario"]
    )

    return dados
