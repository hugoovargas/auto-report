import pandas as pd

def calcular_faturamento_total(vendas: pd.DataFrame) -> float:
    return float(vendas["faturamento"].sum())


def calcular_quantidade_total(vendas: pd.DataFrame) -> int:
    return int(vendas["quantidade"].sum())


def contar_vendas(vendas: pd.DataFrame) -> int:
    return len(vendas)
