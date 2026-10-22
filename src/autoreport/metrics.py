import pandas as pd

def calcular_faturamento_total(vendas: pd.DataFrame) -> float:
    return float(vendas["faturamento"].sum())


def calcular_quantidade_total(vendas: pd.DataFrame) -> int:
    return int(vendas["quantidade"].sum())


def contar_vendas(vendas: pd.DataFrame) -> int:
    return len(vendas)

def calcular_faturamento_por_produto(vendas: pd.DataFrame,) -> pd.DataFrame:
    """Calcula o faturamento total de cada produto."""
    resultado = (
        vendas
        .groupby("produto", as_index=False)["faturamento"]
        .sum()
        .sort_values("faturamento", ascending=False)
        .reset_index(drop=True)
    )

    return resultado


def calcular_faturamento_por_categoria(vendas: pd.DataFrame,) -> pd.DataFrame:
    """Calcula o faturamento total de cada categoria."""
    resultado = (
        vendas
        .groupby("categoria", as_index=False)["faturamento"]
        .sum()
        .sort_values("faturamento", ascending=False)
        .reset_index(drop=True)
    )

    return resultado
